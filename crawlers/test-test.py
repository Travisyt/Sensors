import re
import os
import xml.dom.minidom as dom
import xml.etree.ElementTree as et
import _elementtree


# list = [1,2,3]
# print(list.__contains__(4))
# list.clear()
# print(list)
#
#
# testStr = "ewq|qwe|ewr"
# print(re.split("\|", testStr))

# testStr = "qwe123"
# testStr1 = "qwe123"
# print(testStr.__eq__(testStr1))
#
# list1 = []
# temp = []
# for i in range(10):
#     temp.clear()
#     for j in range(3):
#         temp.append(j)
#     list1.append(temp)
# print(list1)


# print("I am %s, I am %d year old"%("abc", 123))

# print(not os.path.exists("../test"))

# file = open("../test", "w")
# file.write("123\n")
# file.close()
#
# file = open("../test", "a")
# file.write("ads")
# # file.writelines([["dasd"], ["daswwq"], ["cxzcsa"]])
# file.close()


# src = "asndj"
# inte = 123
# list1 = [1,"asd","ab"]
# print(str(src))
# print(str(inte))
# print(str(list1))
#
# path = os.path.abspath("test.xml")
# contains = dom.parse("test.xml")
# print(contains)
# a = contains.("a")
# print(type(a))
# for item in a:
#     print(item)
#     print(type(item))


# import time
#
# print(time.asctime())
# file = open("../temp/test_2019-09-04_NJH", "w")
# file.write("wer")
# file.close()
#

#
# def fun():
#     print("asdf")
#     list = [[1, 2], [2, 4]]
#     print(type(list[0]))
#
# def main():
#     fun()
#
# if __name__ == '__main__':
#     main()
# import sys
#
# # print(type(sys.argv[1]))
# print(sys.argv[1])
# print(sys.argv[2])
#
# import json
#
# list_char = ['苏州', '上海']
# print(list_char)
# map_char = {"1": "苏州", "2": "上海"}
# print(map_char)
# print(json.dumps(map_char).encode("utf-8"))

# list = [1,2,3]
# def fun(list):
#     for i in list:
#
#
# fun(list)
# print(list)
# def fn(x):
#     return x * x
#
#
# print([x * y for x in range(1, 9) for y in range(1, 9) if x == 1])
# i = 100
# print(not i == 1)

# import logging

import requests
resp = requests.get("https://kyfw.12306.cn/otn/leftTicket/queryA?leftTicketDTO.train_date=2019-10-10&lef"
             "tTicketDTO.from_station=SNH&leftTicketDTO.to_station=NJH&purpose_codes=ADULT")
print(resp.text)

import urllib3