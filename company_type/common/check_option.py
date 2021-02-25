# -*- coding: utf-8 -*-
# @Time    : 2021-02-20 11:47
# @Author  : XU
# @File    : check_option.py
# @Software: PyCharm
import os
import xlrd
import time
import requests
from company_type.common.setting import URL
from company_type.common.connection import connect_db

headers = {
    'Content-Type': 'application/json',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}


def get_responce(assert_data):
    """获取接口response"""
    types = list()
    response = requests.post(url=URL, json=assert_data, headers=headers)
    # print(f"接口状态码： {response.status_code}")
    json_data = response.json()
    for key in json_data["data"]:
        result = json_data["data"][key]
        types.append((result, key))
    return types


def check_result(types, expect_result):
    """校验公司类型"""
    for actual_result in types:
        try:
            assert actual_result[0] == expect_result, f"索引：{types.index(actual_result)}"
        except:
            print(f"疑问gid：{actual_result[1]}")


def get_company(company_type):
    """获取公司名"""
    path = os.path.dirname(os.path.dirname(__file__))
    filename = f"{path}/Data/{company_type}.xlsx"
    company_data = xlrd.open_workbook(filename=filename)
    company = company_data.sheet_by_name(sheet_name="高级搜索")
    return list(company.row_values(i)[0] for i in range(3, company.nrows))


def get_cid(company_list):
    """获取cid"""
    cid_list = list()
    db = connect_db()
    for company in company_list:
        sql = f"SELECT id FROM company WHERE `name`='{company}';"
        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                cid = cursor.fetchall()[0][0]
                cid_list.append(cid)
        except:
            print(company)
    return cid_list


def get_gid(cid_list):
    """获取gid"""
    gid_list = list()
    db = connect_db()
    for cid in cid_list:
        sql = f"SELECT graph_id from company_graph WHERE company_id='{cid}';"
        try:
            with db.cursor() as cursor:
                cursor.execute(sql)
                gid = cursor.fetchall()[0][0]
                gid_list.append(gid)
        except:
            print(cid)
    return gid_list


if __name__ == '__main__':
    company_type = "NPO"

    """获取gid"""
    # compeny_list = get_company(company_type=company_type)
    # print(f"====公司名：{compeny_list} ")
    #
    # cid_list = get_cid(company_list=compeny_list)
    # print(f"====cid：{cid_list} ===")
    #
    # gid_list = get_gid(cid_list=cid_list)
    # print(f"====gid：{gid_list} ===")
    #
    # with open(f'./{company_type}.txt', 'w', encoding='utf-8') as file:
    #     file.write(str(gid_list))

    """校验类型"""
    with open(f'./{company_type}.txt', 'r', encoding='utf-8') as file:
        data = file.readline().replace('[', '').replace(']', '').split(', ')
    step = 25
    for i in range(200):
        s = i * step
        e = s + step
        types = get_responce(assert_data=data[s:e])
        time.sleep(2)
        check_result(types=types, expect_result=company_type)

result = {
    "NORMAL":  "3393651442",
    "HKCOMPANY": "3084248661",
    "NPO":  "4208832288",
    "LAWFIRM": "3349259739",
    "GOVERNMENT": "3098128463",
    "FINANCE": "3078806058",
    "TWCOMPANY":  "3209333553",
    "PTY": "3020940523",
    "WOE": "3211602095",
    "PAERNERSHIP": "894123050"
}

"""

"": "PARTNERSHIP",
"": "PTY",
"": "GOVERNMENT",
"": "NORMAL",
"": "NPO",
"": "HKCOMPANY",
"": "TWCOMPANY",


"http://qyxy.baic.gov.cn/": "NORMAL",
"npo": "NPO",
"institution": "GOVERNMENT",
"npo_foundation": "FINANCE"
"http://qyxy.baic.gov.cn/":	"PARTNERSHIP"
"http://qyxy.baic.gov.cn/": "PTY"
"hk_2296000": "HKCOMPANY"
"tw_68067105_factory": "TWCOMPANY"




"""