import xlrd
from python.pythonxiangmu.实战.config_Utils import *


class ReadExcel:
    def __init__(self, execl_path):
        self.execl_path = execl_path

    def all_read_excel_info_in(self):
        workbook = xlrd.open_workbook(self.execl_path)
        sheet = workbook.sheet_by_index(0)
        all_read_excel_info = []
        for i in range(1, sheet.nrows):
            read_excel_info = []
            for j in range(0, sheet.ncols):
                read_excel_info.append(sheet.cell_value(i, j))
            all_read_excel_info.append(read_excel_info)
        return all_read_excel_info


if __name__ == "__main__":
    corrunt = os.path.dirname(__file__)
    config = ConfigUitl()
    EXCEL_path = config.get_excel_path()
    print(EXCEL_path)
    read_excel = ReadExcel(EXCEL_path)
    value = read_excel.all_read_excel_info_in()
    for i in range(len(value)):
         print(value[i])
