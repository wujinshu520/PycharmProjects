import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

courrent = os.path.dirname(__file__)
chrome_driver_path = os.path.join(courrent, '../webdriver/chromedriver')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")

# 登录的账户名
driver.find_element(By.XPATH, '//input[@id ="account"]').send_keys("test01")
time.sleep(3)  # 睡眠3秒

# 清除表单
# driver.find_element(By.XPATH, '//input[@id ="account"]').clear()

# 登录的密码
driver.find_element(By.XPATH, '//input[@name ="password"]').send_keys('newdream123')
time.sleep(2)
# 点击登录按钮
# driver.find_element(By.XPATH, '//button[@id ="submit"]').click()

# driver.find_element(By.XPATH, '//form[@target ="hiddenwin"]').submit()  # 类似做了点击登录
# 1、提交表单  2、解决有些大表单提交按钮在浏览器下方固定隐藏

# size: 返回对象的尺寸
size = driver.find_element(By.XPATH, '//input[@name ="password"]').size
print(size)

# text: 返回对象的文本
text = driver.find_element(By.XPATH, '//button[@id ="submit"]').text
print(text)

# get_attribute('属性名')： 获取对象的属性值
value = driver.find_element(By.XPATH, '//button[@id ="submit"]').get_attribute('data-loading')
print(value)

value = driver.find_element(By.XPATH, '//button[@id ="submit"]').get_property('data-loading')
print(value)

# is_displayed() 用来判断对象是否可见，即css的display属性是否为none
is_dis = driver.find_element(By.XPATH, '//button[@id ="submit"]').is_displayed()
print(is_dis)

# is_enabled() 判断对象是否禁用
is_en = driver.find_element(By.XPATH, '//button[@id ="submit"]').is_enabled()
print(is_en)

# is_selected() 判断对象是否被禁用
is_sele = driver.find_element(By.XPATH, '//input[@name ="keepLogin"]').is_selected()
print(is_sele)

# 截图
driver.find_element(By.XPATH,'//button[@id="subimt"]').screenshot('element.png')

time.sleep(8)
driver.quit()
