import requests
import re
from requests.exceptions import RequestException
requests.packages.urllib3.disable_warnings()

url = 'https://www.12306.cn/index/script/core/common/station_name_v10029.js'

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

js = get_one_page(url, headers)
print(js)
stations = re.findall('([\u4e00-\u9fa5]+)\|([A-Z]+)', js)
print(stations)
file = open("station_names.txt", "w+", encoding='utf-8')
file.truncate()
for station in stations:
    file.write(station[0] + ',')
    file.write(station[1] + '\n')

file.close()

