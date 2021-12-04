# 函数的封装
import os

import xlrd
from python.pythonxiangmu.python对象.python_class.StudentBaseInfo import StudentBaseInfo


class ReadExcel:
    def __init__(self, excel_path):
        self.excel_path = excel_path

    def read_execl_save_list(self):
        workbook = xlrd.open_workbook(self.excel_path)
        sheet = workbook.sheet_by_name('Sheet1')
        all_student_info = []  # 存放所有的数据
        for i in range(1, sheet.nrows):  # 读取的行数
            row_student_info = []  # 存放获得的列表数据
            for j in range(0, sheet.ncols):  # 读取的列数
                row_student_info.append(sheet.cell_value(i, j))
            all_student_info.append(row_student_info)
        return all_student_info

    def read_execl_save_list_obj(self):
        workbook = xlrd.open_workbook(self.excel_path)
        sheet = workbook.sheet_by_name('Sheet1')
        all_student_info = []  # 存放所有的数据
        for i in range(1, sheet.nrows):  # 读取的行数
            student02 = StudentBaseInfo(sheet.cell_value(i, 0),
                                        sheet.cell_value(i, 1),
                                        sheet.cell_value(i, 2),
                                        sheet.cell_value(i, 3),
                                        sheet.cell_value(i, 4))
            all_student_info.append(student02)
        return all_student_info


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../data/学生基本信息.xlsx')
    read_excel = ReadExcel(excel_path)
    cases = read_excel.read_execl_save_list()
    for i in range(len(cases)):
        print(cases[i])

    cases01 = read_excel.read_execl_save_list_obj()
    for i in range(len(cases01)):
        print(cases01[i].name)
