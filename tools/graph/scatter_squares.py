# -*- coding: utf-8 -*-
# @Time    : 2021-01-28 23:18
# @Author  : XU
# @File    : scatter_squares.py
# @Software: PyCharm
import matplotlib.pyplot as plt

x_value = list(range(1, 1001))
y_value = [x**2 for x in x_value]

# plt.scatter(x_value, y_value, c='red', edgecolors='none', s=4)
plt.scatter(x_value, y_value, c=y_value, cmap=plt.cm.Reds, edgecolors='none', s=4)

plt.title("Square Number", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square Of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.axis([0, 1100, 0, 1100000])

plt.show()

