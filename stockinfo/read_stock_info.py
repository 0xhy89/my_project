# -*- coding: utf-8 -*-
# @Time    : 2021-02-01 22:04
# @Author  : XU
# @File    : read_stock_info.py
# @Software: PyCharm
# from __future__ import (absolute_import, division, print_function, unicode_literals)
#
# try:
#     # python 2.x
#     from urllib2 import urlopen
# except ImportError:
#     # python 3.x
#     from urllib.request import urlopen
# import ssl
import requests
import json

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'

# response = urlopen(json_url)
# req = response.read()

# with open('btc_close_2017_urllib.json', 'wb') as f:
#     f.write(req)
#
# file_urllib = json.load(req)
# print(file_urllib)


response = requests.get(url=json_url)
print(response)

with open('data.json', 'w') as f:
    f.write(response.text)

with open('data.json', 'r') as file:
    data_json = json.load(file)
for data in data_json:
    print(f"日期：{data['date']}；月份：{data['month']}；第{data['week']}周；星期：{data['weekday']}；收盘价：{data['close']}")

# for i in res:
#     print(i)
