import os
import time
import xlrd
from selenium import webdriver

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(10)
driver.get("https://www.cnblogs.com/")

workbook = xlrd.open_workbook('../cookies文件/student.xls')
sheet = workbook.sheet_by_name('sheet1')
cookies_list = []
for row_num in range(1, sheet.nrows):
    cookies_dict = {}
    cookies_dict['name'] = sheet.cell_value(row_num, 0)
    cookies_dict['value'] = sheet.cell_value(row_num, 1)
    cookies_dict['path'] = sheet.cell_value(row_num, 2)
    cookies_dict['domain'] = sheet.cell_value(row_num, 3)
    # cookies_dict['httpOnly'] = True if sheet.cell_value(row_num, 4) == 'TRUE' else False
    # cookies_dict['secure'] = True if sheet.cell_value(row_num, 5) == 'TRUE' else False
    cookies_dict['httpOnly'] = bool(sheet.cell_value(row_num, 4))
    cookies_dict['secure'] = bool(sheet.cell_value(row_num, 5))
    cookies_list.append(cookies_dict)
for cookie in cookies_list:
    driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()