# -*- coding: utf-8 -*-
# @Time    : 2021-02-16 23:54
# @Author  : XU
# @File    : urls.py
# @Software: PyCharm
from django.urls import path

from . import views


urlpatterns = [
    # 主页
    path('^$/', views.index, name='index')
]
