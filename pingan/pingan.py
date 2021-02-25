# -*- coding: utf-8 -*-
# @Time    : 2020-08-21 12:09
# @Author  : XU
# @File    : pingan.py
# @Software: PyCharm
import os

dir_path = os.path.abspath(os.path.dirname(__name__))
filename = dir_path + "/pingan.txt"

"""打印平安经"""

pingan_list1 = [f'{i}平安,' for i in ['初生', '满月', '百天']]
pingan_list2 = [f'{i}岁平安,' for i in range(1, 101)]
pingan_list = pingan_list1 + pingan_list2

pingan_list[-1] = pingan_list[-1].replace(',', '。')
pingan_list = ''.join(pingan_list)

title = "\t各年龄平安\n"
pingan_list = title + pingan_list

with open(filename, 'w', encoding='UTF-8') as f:
    f.write(pingan_list)



