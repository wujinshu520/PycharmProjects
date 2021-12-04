import os
import time
import xlwt
from selenium import webdriver

currnt = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(currnt, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get('https://www.csdn.net/')
time.sleep(50)  # 手动输入用户名，密码以及验证码的时间
cookies = driver.get_cookies()
workbook = xlwt.Workbook(encoding='utf-8')  # 创建workbook对象
worksheet = workbook.add_sheet('sheet1')  # 创建工作表sheet1
worksheet.write(0, 0, 'name')  # 往表格中写入内容，第一各参数，行，第二个参数列，第三个参数内容
worksheet.write(0, 1, 'value')
worksheet.write(0, 2, 'path')
worksheet.write(0, 3, 'domain')
worksheet.write(0, 4, 'httpOnly')
worksheet.write(0, 5, 'secure')

for i in range(1, len(cookies) + 1):
    worksheet.write(i, 0, cookies[i - 1]['name'])  # 往表格中写入内容，第一各参数，行，第二个参数列，第三个参数内容
    worksheet.write(i, 1, cookies[i - 1]['value'])
    worksheet.write(i, 2, cookies[i - 1]['path'])
    worksheet.write(i, 3, cookies[i - 1]['domain'])
    worksheet.write(i, 4, cookies[i - 1]['httpOnly'])
    worksheet.write(i, 5, cookies[i - 1]['secure'])
workbook.save('../cookies文件/CSDN.xls')  # 保存表为students.xls
