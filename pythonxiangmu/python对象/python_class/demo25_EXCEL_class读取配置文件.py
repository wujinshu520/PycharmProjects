# 函数的封装
import configparser
import os
import xlrd


class ReadExcel:
    def __init__(self, excel_path):
        self.excel_path = excel_path

    def read_execl_save_list(self):
        workbook = xlrd.open_workbook(self.excel_path)
        sheet = workbook.sheet_by_index(0)  # 错误点
        all_student_info = []  # 存放所有的数据
        for i in range(1, sheet.nrows):  # 读取的行数
            row_student_info = []  # 存放获得的列表数据
            for j in range(0, sheet.ncols):  # 读取的列数
                row_student_info.append(sheet.cell_value(i, j))
            all_student_info.append(row_student_info)

        return all_student_info


if __name__ == '__main__':
    ''' 方式一：'''
    current_path = os.path.dirname(__file__)
    conf = configparser.ConfigParser()
    cfgpath = os.path.join(current_path, '../utils/config.ini')
    conf.read(cfgpath, encoding="utf-8")
    conf.get('default', 'excel_path')
    print(conf.get('default', 'excel_path'))
    excel_path = os.path.join(current_path, conf.get('default', 'excel_path'))
    read_excel = ReadExcel(excel_path)
    cases = read_excel.read_execl_save_list()
    for i in range(len(cases)):
        print(cases[i])

    ''' 方式二：
    
    current_path = os.path.dirname(__file__)
    conf = configparser.ConfigParser()
    cfgpath = os.path.join(current_path, '../utils/config.ini')
    conf.read(cfgpath, encoding="utf-8")
    conf.get('default', 'excel_path')
    read_excel = ReadExcel(conf.get('default', 'excel_path'))
    cases = read_excel.read_execl_save_list()
    for i in range(len(cases)):
        print(cases[i])
    
    
    '''