# -*- coding: utf-8 -*-
# @Time    : 2021-02-21 11:31
# @Author  : XU
# @File    : start.py
# @Software: PyCharm
import os
import sys

sys.path.append(os.path.abspath(__file__).split("my_api")[0])

from my_api.config import setting
from my_api.lib.interface import my_app

# from flup.server.fcgi import WSGIServer

my_app.secret_key = setting.SECRET_KEY
if __name__ == '__main__':
    # WSGIServer(my_app, bindAddress=(setting.SERVER_HOST, setting.SERVER_PORT)).run()
    my_app.config['JSON_AS_ASCII'] = False
    my_app.run(host=setting.SERVER_HOST, port=setting.SERVER_PORT, debug=False)
