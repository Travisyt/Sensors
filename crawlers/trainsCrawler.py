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
for src in stations:
    for dest in stations:
        if(src == stations):
            break
        print(src + dest)

    if(src == dest):
        break





