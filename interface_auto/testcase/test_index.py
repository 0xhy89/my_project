# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 23:23
# @Author  : XU
# @File    : test_index.py
# @Software: PyCharm
import allure
import pytest
from interface_auto.provider.common import get_response, check_data
from interface_auto.data.api import url


@allure.feature("首页")
@pytest.mark.usefixtures()
class Test:

    @allure.title("热门公司")
    def test_hot_company(self):
        with allure.step(f"请求接口:{url['hot_word']}"):
            result = get_response(url=url["hot_word"], headers=self.headers)
        with allure.step("获取字段"):
            check_data(result=result)
        assert result['state'] == 'ok'

