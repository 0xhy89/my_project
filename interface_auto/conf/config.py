# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 23:27
# @Author  : XU
# @File    : config.py
# @Software: PyCharm
import os

headers = {
    "Authorization": "0###oo34J0ZgbSD7ufsu_CV7Cl1yyT4A###1543998038367###49bf6ec42afb289fbeed4933518c1325",
    "version": "TYC-XCX-WX",
    "Content-Type": "application/json"
}

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 测试报告目录
REPORT_DIR = os.path.join(BASE_DIR, "report")
# 测试用例目录
TESTCASE_DIR = os.path.join(BASE_DIR, "testcase")
