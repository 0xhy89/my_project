# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 23:27
# @Author  : XU
# @File    : common.py
# @Software: PyCharm
import os
import json
import requests
from interface_auto.conf.config import TESTCASE_DIR


def get_testcast():
    start_name = "test_"
    end_name = ".py"
    cases_list = list()
    for root, dirs, file in os.walk(TESTCASE_DIR):
        for f in file:
            if f.startswith(start_name) and f.endswith(end_name):
                cases_list.append(f"{root}/{f}")
    return cases_list


def get_response(url, headers):
    r = requests.get(url=url, headers=headers)
    content = r.content.decode(encoding='utf8')
    result = json.loads(content)
    return result
