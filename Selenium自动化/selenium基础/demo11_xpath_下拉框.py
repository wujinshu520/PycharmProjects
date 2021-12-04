import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
page_path = os.path.join(current, '../page_path/wait.html')

driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get('file://' + page_path)
driver.implicitly_wait(10)
driver.find_element(By.XPATH, '//button').click()

# 1、下拉框通过元素定位识别
driver.find_element(By.XPATH, '//option[value="orange"]').click()

# 2、通过下拉框对象内置的方法去选择
select_element = driver.find_element(By.XPATH, '//select[@id="Selector"]')
select_el = Select(select_element)  # 强制转换
select_el.select_by_visible_text('葡萄')
time.sleep(1)
select_el.select_by_value('peach')
time.sleep(1)
select_el.select_by_index(5)
