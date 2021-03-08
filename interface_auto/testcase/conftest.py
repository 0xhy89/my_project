# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 23:13
# @Author  : XU
# @File    : conftest.py
# @Software: PyCharm
import pytest

from interface_auto.conf.config import url, headers


@pytest.fixture(scope="class", autouse=True)
def setup_class(request):
    request.cls.headers = headers
    request.cls.url = url


@pytest.fixture(scope="function", autouse=True)
def setup_function():
    pass