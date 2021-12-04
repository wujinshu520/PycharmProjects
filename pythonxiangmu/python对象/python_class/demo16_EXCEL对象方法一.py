# 2、读取数据保存为对象
# all_student_info=【对象1，对象2，对象3】

import os
import xlrd
from python.pythonxiangmu.python对象.python_class.StudentBaseInfo import StudentBaseInfo

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../data/学生基本信息.xlsx')
print(excel_path)

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('Sheet1')
all_student_info = []  # 存放所有的数据

# ---------方式一： 一个个获取保存-------
student01 = StudentBaseInfo(sheet.cell_value(1,0),
                            sheet.cell_value(1,1),
                            sheet.cell_value(1,2),
                            sheet.cell_value(1,3),
                            sheet.cell_value(1,4))
all_student_info.append(student01)
print(all_student_info[0].name)

