# coding:utf-8
import re
import requests
import os
import sys
import xml.dom.minidom as dom
import time

'''
    
    传入参数：出发站 到达站 出发日期
    生成：log、_SUCCESS_{timemilli} 标志文件、列车列表文件
    
'''


# os.chdir("C:/Users/YT/Desktop/structure/bin")

# file write
def file_output(filename, src, mode="a+"):
    temp = []
    file = open(filename, mode, encoding="utf-8")
    if type(src) == type(temp):
        if type(src[0]) == type(temp):
            for item in src:
                for item_item in item:
                    file.write(str(item_item) + "\t")
                file.write("\n")
        else:
            for item in src:
                file.write(str(item) + "\n")
    else:
        file.write(str(src) + "\n")

    file.close()


def index_out(src, dst, date, index):
    index_path = "../temp/indexes/"
    temp = "\"index\":\"" + index + "\"\t" + "\"updatetime\":\"" + str(int(time.time())) + "\""
    file_output(index_path + date + "_" + src + "_" + dst, temp, mode="w+")


def getkey(index):
    key_dict = {3: "tranid", 4: "from", 5: "to", 6: "depart", 7: "arri", 8: "deptime",
                9: "arritime", 10: "timecost", 13: "date", 25: "noseat", 29: "seseat",
                30: "firstseat", 31: "bussiseat"}
    return key_dict.get(index)


class mainCrawler:
    output_path = "../temp/transinfos/"

    index_path = "../temp/indexes/"

    conf_path = "../conf/"

    log_path = "../log/"

    # output_path = "../temp/"
    #
    # index_path = "../temp/"
    #
    # conf_path = "../temp/"
    #
    # log_path = "../temp/"

    # 构造函数不写业务信息， 以保证单例
    def __init__(self):
        # 结果信息
        self.trans_info = []
        self.is_high_rail = False
        self.timemilli = 0
        self.time_out = 10

    def get_trans_info(self, src, dst, date):
        cookies = ''
        # 测试请求
        # pre_url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs=上海,SHH&ts=成都,CDW&date={date}&flag=N,N,Y'

        url = "https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicke" \
              "tDTO.train_date={date}&leftTicketDTO.from_station={from_station}&" \
              "leftTicketDTO.to_station={to_station}&purpose_codes=ADULT"

        # url = "https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2019-10-10&leftTicketDTO.from_stati" \
        #       "on=SNH&leftTicketDTO.to_station=NJH&purpose_codes=ADULT"

        # 请求头
        headers = {
            'Host': 'kyfw.12306.cn',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0',
            'If-Modified-Since': '0',
            'Connection': 'keep-alive',
            'Cookie': cookies
        }
        # pre_url = pre_url.format(date=date)
        url = url.format(date=date, from_station=src, to_station=dst)
        session = requests.session()
        session.headers = headers
        # 第一次模拟游客登陆，获取cookies
        # session.get(pre_url, timeout=20)
        # 第二次伪装成同一个游客请求
        # session.headers = headers
        try:
            response = session.get(url, timeout=self.time_out)
        except:
            mainCrawler.log(time.asctime() + "\tFailed\tCausedby : timeout or refused\t" + date + "_" + src + "_" + dst,
                            mode=0)
            return False

        jsn = response.text

        print(response.status_code)
        # 如果空， 退出， 写入日志
        if response.status_code != 200:
            if response.status_code == 302:
                mainCrawler.log(time.asctime() + "\tFailed\tCausedby : 302 redirect\t" + date + "_" + src + "_" + dst,
                                mode=0)
                # print(response.text)
                # print(url)
            elif response.status_code == 404:
                mainCrawler.log(time.asctime() + "\tFailed\tCausedby : 404 PageNotFound\t" + date + "_" + src + "_" + dst,
                                mode=0)
            else:
                mainCrawler.log(time.asctime() + "\tFailed\tCausedby : unknown\t" + date + "_" + src + "_" + dst,
                                mode=0)
            return False

        # prehandle
        # print(jsn)
        # 找到json中的结果集字符串, 并将各列车信息放入list
        jsonString = re.findall("\"result\":\\[(.*?)\\]", jsn)[0]
        transInfoList = re.findall("\"(.*?)\"", jsonString)

        # after prehandle
        # print(transInfoList)
        # print("总数：" + str(transInfoList.__len__()))

        # 处理冗余数据

        # 有用的信息列表
        '''
            错误方式: 在此处声明afterHandledList = [] 
            因为全局变量是引用类型，导致最后的结果集中存放的是相同的数据
        '''
        # 列表中有用的索引号
        usefulIndex = [3, 4, 5, 6, 7, 8, 9, 10, 13, 25, 29, 30, 31]
        # 处理后的列车信息列表
        handledTransInfoList = []

        for tranInfo in transInfoList:
            tranInfoList = re.split("\\|", tranInfo)
            # 分割信息列表的索引， 用来定位有用的信息
            # 索引归零
            infoIndex = 0
            # 清空单次列车信息列表
            afterHandledList = []
            for item in tranInfoList:
                # 遇到有用信息就导入信息列表
                if usefulIndex.__contains__(infoIndex):
                    # 获取标签
                    key_str = getkey(infoIndex)
                    # 遇到无票处理为“无”
                    if item.__eq__(""):
                        item = "无"
                    item = "\"" + key_str + "\":" + "\"" + item + "\""
                    afterHandledList.append(item)
                infoIndex += 1
            # 单次列车信息注入列表
            # 错误原因
            handledTransInfoList.append(afterHandledList)

        self.trans_info = handledTransInfoList
        print("high rail:" + str(self.is_high_rail) + "\nresult:" + str(handledTransInfoList))
        return handledTransInfoList

    '''
    # DEMO
    print(get_trans_info("SNH", "NJH", "2019-09-20"))


    # 更新索引表
    def index_out(self, src, dst, date):
        path = output_path + date + "_" + src + "_" + dst
        file_output()


    def get_conf(self, file):
        dom_tree = dom.parse(conf_path + file)
        contains = dom_tree.documentElement

    '''

    @staticmethod
    def log(text, mode=0):
        '''
        mode:
            0:公用log
            1:
            2:
        '''
        if mode == 0:
            file_output(mainCrawler.log_path + "main.log", text, "a")

    # 输出到文件
    def output(self, src, dst, date):
        self.timemilli = str(int(time.time()))
        path = mainCrawler.output_path + self.timemilli + "_" + date + "_" + src + "_" + dst
        if not os.path.exists(path):
            file_output(path, mode="w", src=self.trans_info)
            # 更新索引
            index_out(src, dst, date, path)
            file_output(mainCrawler.output_path + "_SUCCESS_transinfo_", mode="w", src="")
            mainCrawler.log(time.asctime() + "\tSuccessed\t" + date + "_" + src + "_" + dst, mode=0)
        else:
            mainCrawler.log(time.asctime() + "\tFailed Causedby : file already exist\t" + date + "_" + src + "_" + dst,
                            mode=0)
            raise RuntimeError("file already exist")


def main():
    """

    :rtype: object
    """
    # 获取上层调用传参
    src = sys.argv[1]
    dst = sys.argv[2]
    date = sys.argv[3]

    # 测试
    # src = "NJH"
    # dst = "SNH"
    # date = "2019-09-12"

    ms = mainCrawler()
    if not ms.get_trans_info(src, dst, date):
        return
    ms.output(src, dst, date)


if __name__ == '__main__':
    main()
