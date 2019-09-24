import requests
import re

from requests.exceptions import RequestException


def fileo(name, contains):
    file = open(name, "w", encoding="utf-8")
    file.truncate()
    file.write(contains)
    file.close()


# ================发送请求函数================== #
def get_one_page(url, headers=True):  # 打开页面并抛出错误
    try:
        if headers:
            response = requests.get(url)
        else:
            response = requests.get(url, headers=headers)
        if response.status_code == 200:
            response.encoding = 'utf-8'
            return response.text
        return None
    except RequestException:
        return None


# ================请求头编写================== #
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:68.0) Gecko/20100101 Firefox/68.0'}

# ================URL 保留占位符================== #
# url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={src},AOH&ts={dst},NJH&date={date}&flag=N,N,Y'
url = 'https://kyfw.12306.cn/otn/leftTicket/init?linktypeid=dc&fs={0},AOH&ts={1},NJH&date={2}&flag=N,N,Y'
# ================拼接URL串================== #
src = ""
dst = ""
date = ""

src = "上海虹桥"
dst = "南京"
date = "2019-09-05"

# url.replace("{src}", src)
# url.replace("{dst}", dst)
# url.replace("{date}", date)
url = url.format(src, dst, date)

# ================发送请求================== #

# html = get_one_page(url, headers)
html = get_one_page(url)
fileo("out", html)
print(html)
print(url)
