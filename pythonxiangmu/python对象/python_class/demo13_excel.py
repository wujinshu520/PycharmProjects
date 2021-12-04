# excel操作
# 使用xlrd模块：第三方的工具包，可以读取xlsx，xls的excel文件   xlwt模块用于写入

import xlrd

# 创建工作薄对象
workbook = xlrd.open_workbook('/Users/zhang/Desktop/PycharmProjects/python/pythonxiangmu/python对象/data/学生基本信息.xlsx')

# 创建表格对象
sheet = workbook.sheet_by_name('Sheet1')  # 注意区别大小写
print('总行数：', sheet.nrows)
print('总列数：', sheet.ncols)
print('第一行的数据', sheet.row(0))  # 行和列的下标都是从0开始
print('单元格子的数据：',sheet.cell_value(1,1)) # 行、列
# 类型：0-5 依次表示：0-空，1-string()，2-number，3-date，4-bool，5-error
print('单元格的类型：',sheet.cell_type(3,1))
