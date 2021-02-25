# -*- coding: utf-8 -*-
# @Time    : 2021-01-23 17:27
# @Author  : XU
# @File    : excel_operation.py
# @Software: PyCharm
import os
import xlrd


class ExcelOperation:

    def readExcel(self):
        base_path = os.path.dirname(__file__)
        filename = base_path + '/data.xlsx'
        print(filename + "--")

        excel = xlrd.open_workbook(filename=filename)

        data = excel.sheet_by_name(sheet_name="data")
        row_count = data.nrows
        print(row_count)

        result = list()
        element = dict()
        for i in range(row_count):
            key = data.row_values(i)[0]
            value = data.row_values(i)[1]
            element[key] = value
            result.append(data.row_values(i)[2])
        return element, result


if __name__ == '__main__':
    eo = ExcelOperation()
    element, result_list = eo.readExcel()
    for key in element.keys():
        if element[key] % 2 == 1:
            print("奇数")
        else:
            print("偶数")
