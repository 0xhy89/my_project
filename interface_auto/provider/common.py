# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 23:27
# @Author  : XU
# @File    : common.py
# @Software: PyCharm
import os
import json
import requests
from interface_auto.conf.config import TESTCASE_DIR
from interface_auto.conf.config import headers, mobile
from interface_auto.data.api import url, api9


def get_testcast():
    start_name = "test_"
    end_name = ".py"
    cases_list = list()
    for root, dirs, file in os.walk(TESTCASE_DIR):
        for f in file:
            if f.startswith(start_name) and f.endswith(end_name):
                cases_list.append(f"{root}/{f}")
    return cases_list


def analysis_report():
    pass


def login():
    sms_code_result = get_response(url=url["sms_code"], headers=headers)
    sms_code = sms_code_result["data"]
    print(f"验证码是：{sms_code}")
    login_result = get_response(url=url["login"].format(api9, sms_code, mobile), headers=headers)
    print(login_result)


def get_response(url, headers):
    r = requests.get(url=url, headers=headers)
    content = r.content.decode(encoding='utf8')
    result = json.loads(content)
    return result


def check_data(result):
    for i in range(len(result["data"])):
        data = result["data"][i]
        for key in data.keys():
            print(key)
