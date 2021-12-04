import os
import time

import xlrd
from selenium import webdriver
from selenium.webdriver.common.by import By

currnt = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(currnt, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(20)
driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")
time.sleep(3)  # 手动输入用户名，密码以及验证码的时间

workbook = xlrd.open_workbook('../cookies文件/zentao.xls')
sheet = workbook.sheet_by_name('sheet1')
cookies_list = []
for row_num in range(1, sheet.nrows):
    cookies_dict = {}
    cookies_dict['name'] = sheet.cell_value(row_num, 0)
    cookies_dict['value'] = sheet.cell_value(row_num, 1)
    cookies_dict['path'] = sheet.cell_value(row_num, 2)
    cookies_dict['domain'] = sheet.cell_value(row_num, 3)
    cookies_dict['httpOnly'] = bool(sheet.cell_value(row_num, 4))
    cookies_dict['secure'] = bool(sheet.cell_value(row_num, 5))
    cookies_list.append(cookies_dict)
for cookie in cookies_list:
    driver.add_cookie(cookie)
time.sleep(3)
driver.refresh()

# 用如下方法不好，因为禅道属于支持国际化语言的项目

driver.find_element(By.XPATH, '//a[contains(@href,"zentao/www/index.php?m=qa")]').click()
driver.find_element(By.XPATH, '//a[contains(@href,"zentao/www/index.php?m=bug")]').click()
driver.find_element(By.XPATH, '//a[contains(@href,"zentao/www/index.php?m=bug&f=create")]').click()

# 思考，最好是用文本，因为都是测试要输入的数据

# 所属产品
driver.find_element(By.XPATH, '//div[@id="product_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="学生成绩管理系统"]').click()
time.sleep(3)

# 所属模块
driver.find_element(By.XPATH, '//div[@id="module_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="/年级成绩管理"]').click()
# driver.find_element(By.XPATH, '//div[@id="module_chosen"]/div/ul/li[2]').click()
time.sleep(3)

# 所属版本
driver.find_element(By.XPATH, '//div[@id="project_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="湖南中医药测试实训"]').click()
time.sleep(3)

# 影响版本
driver.find_element(By.XPATH, '//div[@id="openedBuild_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="v2.0"]').click()

# 当前指派
driver.find_element(By.XPATH, '//div[@id="assignedTo_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="D:开发人员1"]').click()

# 截止日期
driver.find_element(By.XPATH, '//input[@name="deadline"]').send_keys("2021-09-05")

# 错误类型
driver.find_element(By.XPATH, '//div[@id="type_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="设计缺陷"]').click()

# 操作系统
driver.find_element(By.XPATH, '//div[@id="os_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="Windows 7"]').click()

# 浏览器版本
driver.find_element(By.XPATH, '//div[@id="browser_chosen"]').click()
driver.find_element(By.XPATH, '//li[@title="IE系列"]').click()

# bug标题
driver.find_element(By.XPATH, '//input[@name="title"]').send_keys("错误密码能进行登录123321")

# 严重程度
driver.find_element(By.XPATH, '//div[@data-type="severity"]').click()
driver.find_element(By.XPATH, '//span[@data-value="4"]').click()

# 优先级
driver.find_element(By.XPATH, '//div[@data-type="pri"]').click()
driver.find_element(By.XPATH, '//span[@data-value="4" and contains(@class,"label-pri")]').click()
time.sleep(3)

# 输入bug的内容
# 切框架
fr = driver.find_element(By.XPATH, '//iframe[@class="ke-edit-iframe"]')
driver.switch_to.frame(fr)

# 清除内容
driver.find_element(By.XPATH, '/html/body').clear()

# 输入内容
driver.find_element(By.XPATH, '/html/body').send_keys("<p>[步骤]</p>第一步：输入密码<br>")
driver.switch_to.default_content()

# 浏览器滚动操作
time.sleep(2)
element = driver.find_element(By.XPATH, '//div[@id ="mailto_chosen"]')
driver.execute_script('arguments[0].scrollIntoView();', element)
element.click()
time.sleep(2)

# driver.find_element(By.XPATH, '//*[@id="mailto_chosen"]/div/ul/li[4]').click()
driver.find_element(By.XPATH, '//div[@id ="mailto_chosen"]/div/ul/li[@title="T:测试人员2"]').click()


driver.find_element(By.XPATH, '//input[@name="keywords"]').send_keys("密码")

# 保存
driver.find_element(By.XPATH, '//button[@id="submit"]').click()
