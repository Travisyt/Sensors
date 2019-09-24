import re
import requests
from requests.exceptions import RequestException

def get_one_page(url, headers):     #打开页面并抛出错误
    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'}

srcName = '上海虹桥'
destName = '南京'
date = '2019-6-6'
isStu = 'N'
isHigh = 'Y'

file = open("station_names.txt", "r", encoding='utf-8')
stations = []
temp = ''
while(True):
    temp = file.readline()
    temp = re.match('.*', temp).group()
    if(temp):
        stations.append(temp)
    else:
        break
file.close()
print(stations)
for i in range(2862):
    temp = re.match('[\u4e00-\u9fa5]*', stations[i]).group()
    if(temp.encode().decode('utf-8') == srcName.encode().decode('utf-8')):
        srcName = stations[i].encode('gbk').decode('gbk')
        print(srcName)
    elif(temp.encode().decode('utf-8') == destName.encode().decode('utf-8')):
        destName = stations[i].encode('gbk').decode('gbk')
        print(destName)

url = ('https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={}&ts={}&date={}&flag={},{},Y').format(srcName, destName, date, isStu, isHigh)
print(url)
html = get_one_page(url, headers)
print(html)
fileO = open("htmltemp.txt", "w+", encoding='utf-8')
fileO.write(html)
fileO.close()

