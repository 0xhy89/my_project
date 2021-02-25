# -*- coding: utf-8 -*-
# @Time    : 2021-02-20 11:48
# @Author  : XU
# @File    : connection.py
# @Software: PyCharm
import pymysql


def connect_db():
    db_config = {
        "host": "jindiprismproduct.mysql.rds.aliyuncs.com",
        "port": 3306,
        "database": "prism1",
        "user": "jindi",
        "password": "jindichangsheng",
        "charset": "utf8",
    }
    db = pymysql.connect(**db_config)
    return db



