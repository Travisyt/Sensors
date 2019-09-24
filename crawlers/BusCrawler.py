import re
import requests


url = "http://www.chebada.com/busList/GetBusSchedules"

# 巴士管家非 json 传输数据
# # post请求 json 数据包    通过分析火狐网络数据传输得出


request_body = {"departure": "苏州", "destination": "南京客运站", "departureDate": "2019-09-10"}

req_str = "departure=苏州&destination=南京客运站&departureDate=2019-09-09"



headers = {
    'Host': 'www.chebada.com',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv????68.0) Gecko/20100101 Firefox/68.0',
    'Accept': '*/*',
    'Accept-Language': 'zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    # 'X-Tingyun-Id': 'dXavpgQY8Xk;r=996097790',
    # 'Content-Length': '111',
    'Connection': 'keep-alive',
    # 'Cache-Control': 'max-age=0'
}


contains = requests.post(url, data=request_body)

file = open("busout", "w", encoding="utf-8")
file.truncate()
file.write(contains.text)
file.close()


print(contains.text)
