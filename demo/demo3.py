# -*- coding: utf-8 -*-
# @Time    : 2020-09-17 21:52
# @Author  : XU
# @File    : demo3.py
# @Software: PyCharm

# a = 10**31
# print(a)
#
# # ll = [i for i in ll0]
# # ll.extend(ll0)
# # print(ll)
# for i in range(1, 32):
#     print(10**i)
#
#
# print(70/100)

# x = 123
# x = -123
# x = 120
x = 1534236469


def demo(x):
    if -10 < x < 10:
        return x
    x_str = str(x)
    if x > 0:
        x_str = x_str[::-1]
        x = int(x_str)
    else:
        x_str = x_str[:0:-1]
        x = 0 - int(x_str)
    return x if -2**31 < x < 2**31 - 1 else 0


print(demo(x))


