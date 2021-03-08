# -*- coding: utf-8 -*-
# @Time    : 2021-03-08 12:20
# @Author  : XU
# @File    : api.py
# @Software: PyCharm
from interface_auto.conf.config import mobile, sign_6

api9 = "https://api9.tianyancha.com"
capi = "https://capi.tianyancha.com"

url = {
    # 登录
    "sms_code": f"{api9}/services/v3/user/verify/{mobile}/SMS?funtype=1&clientId=199406260020&sign={sign_6}",
    "login": "{}/services/v3/thirdParty/bindPhone?smsCode={}&mobile={}",

    # 首页
    "hot_word": f"{api9}/services/v3/hotSearch/wxHotWord"

}
