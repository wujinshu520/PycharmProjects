# 读取Excel的数据保存为列表、对象
import os, xlrd

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../data/学生基本信息.xlsx')
print(excel_path)

# 1、读取数据保存为列表
# [[学号，姓名，年龄...],[学号，姓名，年龄...],[],[]]
# 外部一个列表元素一个用例，内部列表就是用例详情

workbook = xlrd.open_workbook(excel_path)
sheet = workbook.sheet_by_name('Sheet1')
all_student_info = []  # 存放所有的数据
print(sheet.ncols, sheet.nrows)  # 总行数、总列数
for i in range(1,   sheet.nrows):  # 读取的行数
    row_student_info = []
    for j in range(sheet.ncols):  # 读取的列数
        row_student_info.append(sheet.cell_value(i, j))
    all_student_info.append(row_student_info)

for i in range(len(all_student_info)):
    print(all_student_info[i])
