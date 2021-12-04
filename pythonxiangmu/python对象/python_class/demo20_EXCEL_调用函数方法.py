from python.pythonxiangmu.python对象.python_class.demo19_EXCEL_函数封装调用 import *

current_path = os.path.dirname(__file__)
excel_path = os.path.join(current_path, '../data/学生基本信息.xlsx')

case = read_execl_save_list(excel_path)
print(case)

for i in range(len(read_execl_save_list(excel_path))):
    print(read_execl_save_list(excel_path)[i])

for i in range(len(read_execl_save_list_obj(excel_path))):
        print(read_execl_save_list_obj(excel_path)[i].name)