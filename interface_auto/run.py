# -*- coding: utf-8 -*-
# @Time    : 2021-03-02 22:58
# @Author  : XU
# @File    : run.py
# @Software: PyCharm
import os
import time
import pytest
from interface_auto.provider.common import get_testcast
from interface_auto.conf.config import REPORT_DIR

now = time.strftime("%Y-%m-%d_%H-%M-%S")

allure_dir = f"{REPORT_DIR}/allure/{now}"
if not os.path.exists(allure_dir):
    os.makedirs(allure_dir)

# case = "/Users/xu/Documents/workspace/my_project/demo/interface_auto/testcase/test_01.py"


if __name__ == '__main__':
    for case in get_testcast():
        parameter = [
            case,
            "-s",
            "-v",
            f"--alluredir={allure_dir}",
        ]
        pytest.main(parameter)

    os.system(f"allure generate {allure_dir}/ -o {allure_dir}/html")
