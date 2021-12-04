import os
import time
import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By

currnt = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(currnt, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")
time.sleep(3)  # 手动输入用户名，密码以及验证码的时间

# 登录的账户名
driver.find_element(By.XPATH, '//input[@id ="account"]').send_keys("test01")
time.sleep(3)  # 睡眠3秒

# 登录的密码
driver.find_element(By.XPATH, '//input[@name ="password"]').send_keys('newdream123')
time.sleep(2)

# 点击登录按钮
driver.find_element(By.XPATH, '//button[@id ="submit"]').click()

time.sleep(20)
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

workbook.save('../cookies文件/zentao.xls')  # 保存表为students.xls
