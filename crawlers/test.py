import requests
import json
import re


def fileo(name, contains):
    file = open(name, "w", encoding="utf-8")
    file.truncate()
    file.write(contains)
    file.close()


# # format方法
#
# str1 = "sajhda{name}sadas"
#
# str1 = str1.format(name='BAX')
#
# print(str1)
#
# print("this is {name}".format(name="format"))

src = "AOH"
dst = "NKH"
date = "2019-09-10"

# 测试请求
url = "https://kyfw.12306.cn/otn/leftTicket/queryT?leftTicketDTO.train_date={date}&leftTicketDTO.from_station={from_station}&leftTicketDTO.to_station={to_station}&purpose_codes=ADULT"
url = url.format(date=date, from_station=src, to_station=dst)
response = requests.get(url)
jsn = response.text

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
            # 遇到无票处理为“无”
            if item.__eq__(""):
                item = "无"
            afterHandledList.append(item)
        infoIndex += 1
    # 单次列车信息注入列表
    # 错误原因
    handledTransInfoList.append(afterHandledList)

print(handledTransInfoList)

