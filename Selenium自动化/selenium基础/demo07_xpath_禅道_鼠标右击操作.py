import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")
time.sleep(3)

# 创建一个元素对象
element = driver.find_element(By.XPATH, '//ing[comtains(@src,"zt-logo.png")]')
ActionChains(driver).move_to_element(element).perform()

'''

# 登录的账户名
driver.find_element(By.XPATH, '//input[@id ="account"]').send_keys("test01")
time.sleep(3)  # 睡眠3秒

# 登录的密码
driver.find_element(By.XPATH, '//input[@name ="password"]').send_keys('newdream123')
time.sleep(2)

# 点击登录按钮
driver.find_element(By.XPATH, '//button[@id ="submit"]').click()

'''