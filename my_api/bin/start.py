# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 11:31
# @Author  : XU
# @File    : start.py
# @Software: PyCharm
import os
import sys
sys.path.append(os.path.abspath(__file__).split("my_api")[0])

from my_api.config import setting
from my_api.lib.interface import server


server.secret_key = setting.SECRET_KEY
if __name__ == '__main__':
    server.run(host=setting.SERVER_HOST, port=setting.SERVER_PORT, debug=True)
