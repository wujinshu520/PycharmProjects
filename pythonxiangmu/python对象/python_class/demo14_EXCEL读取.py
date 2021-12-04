# 读取excel内容：改进读取路径
import xlrd, os
from python.pythonxiangmu.python对象.python_class.StudentBaseInfo import StudentBaseInfo

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../data/学生基本信息.xlsx')
print(excel_path)

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('Sheet1')
print('单元格子的数据：', sheet.cell_value(1, 0))  # 行、列
student_infos = []
new_01 = StudentBaseInfo(sheet.cell_value(1,0),
                         sheet.cell_value(1,1),
                         sheet.cell_value(1,2),
                         sheet.cell_value(1,3),
                         sheet.cell_value(1,4),)
student_infos.append(new_01)
for o in range(len(student_infos)):
    print(student_infos[o].name)