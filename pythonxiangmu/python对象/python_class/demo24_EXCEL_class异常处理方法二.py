# 函数的封装
import xlrd
from python.pythonxiangmu.python对象.utils.log_utils import *

class ReadExcel:
    def __init__(self, excel_path):
        self.excel_path = excel_path

    def read_execl_save_list(self):
        try:
            workbook = xlrd.open_workbook(self.excel_path)
            logger.info('创建workbook对象成功')
        except FileNotFoundError as e:
            current_path = os.path.dirname(__file__)
            excel_path = os.path.join(current_path, '../data/学生基本信息.xlsx')
            workbook = xlrd.open_workbook(excel_path)
            logger.error('excel文件未找到，使用默认路径文件： %s' % excel_path)
        sheet = workbook.sheet_by_index(0)  # 错误点
        all_student_info = []  # 存放所有的数据
        for i in range(1, sheet.nrows):  # 读取的行数
            row_student_info = []  # 存放获得的列表数据
            for j in range(0, sheet.ncols):  # 读取的列数
                row_student_info.append(sheet.cell_value(i, j))
            all_student_info.append(row_student_info)

        return all_student_info


if __name__ == '__main__':
    current_path = os.path.dirname(__file__)
    excel_path = os.path.join(current_path, '../data/学生基本信息1.xlsx')
    read_excel = ReadExcel(excel_path)
    cases = read_excel.read_execl_save_list()
    print(cases)
