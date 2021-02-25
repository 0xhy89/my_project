# -*- coding: utf-8 -*-
# @Time    : 2020-08-24 13:26
# @Author  : XU
# @File    : monitor.py
# @Software: PyCharm
import requests
import hashlib

passwd = 'xu123456'
passwd_encrypt = hashlib.md5(passwd.encode()).hexdigest()
print(passwd_encrypt)

url = 'http://www.baidu.com'
print(requests.get(url=url))
