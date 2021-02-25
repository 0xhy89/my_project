# -*- coding: utf-8 -*-
# @Time    : 2020-09-16 21:09
# @Author  : XU
# @File    : monitor_daily_report.py
# @Software: PyCharm
import json
import requests
import time

url_select = "http://10.2.20.233:8889/sel_nodes_v2"
url_insert = "http://10.2.20.233:8889/insert_Push"
post_header = {
    "Content-Type": "application/json;charset=UTF-8",
    "Content-Length": '2048',
}

real_date = time.strftime("%Y/%m/%d", time.localtime()).split('/')
date_list = []
for i in real_date:
    if i == real_date[-1]:
        i = str(int(i) - 2)
    date_list.append(i)
modify_date = '/'.join(date_list)
print(modify_date)

# todo 大小月、闰年的计算
# if int(date_data[2]) - 2 < 0:
#     if date_data[1] == '02':
#         if int(date_data[0]) / 4 == 0:
#             pass
#     if date_data[1] in ['01', '03', '05', '07', '08', '10', '12']:
#         pass
#     else:
#         pass

# 获取法律诉讼
risk_data = {"dim_type": 31}
r = requests.get(url=url_select, params=risk_data)
if r.status_code == 200:
    json_data = json.loads(r.content)
    if len(json_data['message']) != 0:
        uuid = json_data['message'][0][0]
        property = json_data['message'][0][1]
        monitor_data = {
            "target_type": risk_data["dim_type"],
            "uuid": uuid,
            "mobile": "12222222244",
            "h_c": "22822",
            "property": property,
            "monitor_start_time": "2020/01/01 00:00:00",
            "push_start_time": "{} 00:00:00".format(modify_date)
        }
        # todo post请求结果400
        r = requests.post(url=url_insert, data=monitor_data, headers=post_header)
        print(r.content)
else:
    print("获取法律诉讼失败")
