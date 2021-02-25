# -*- coding: utf-8 -*-
# @Time    : 2021-01-27 23:09
# @Author  : XU
# @File    : mpl_squares.py
# @Software: PyCharm
import matplotlib.pyplot as plt

input_squares = [1, 2, 3, 4, 5]
squares = [1, 4, 9, 16, 25]

# 传入输入序列和输出结果，仅提供输出结果会造成，方法plot通过默认方式计算错误
plt.plot(input_squares, squares, linewidth=5)

plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Of Value", fontsize=14)

plt.tick_params(axis='both', labelsize=14)
plt.show()
