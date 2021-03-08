# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 23:23
# @Author  : XU
# @File    : test_01.py
# @Software: PyCharm
import allure
import pytest
from interface_auto.provider.common import get_response
from interface_auto.data.api import url


@allure.feature("测试类")
@pytest.mark.usefixtures()
class Test:

    @allure.title("测试用例")
    def test_01(self):
        with allure.step("请求接口"):
            result = get_response(url=url["hot_word"], headers=self.headers)
        assert result['state'] == 'ok'


# if __name__ == '__main__':
#     pytest.main(["/Users/xu/Documents/workspace/my_project/demo/interface_auto/testcase/"])
