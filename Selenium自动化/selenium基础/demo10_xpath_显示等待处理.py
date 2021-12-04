import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
page_path = os.path.join(current, '../page_path/wait.html')

driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get('file://' + page_path)
driver.find_element(By.XPATH, '//button').click()
# 显示等待： 在一个时间段内的等待
# 1、比较难写
# 2、只针对一个元素生效
driver_wait = WebDriverWait(driver, 20, poll_frequency=0.5)  # poll_frequency 每隔多长时间的设置
element = driver_wait.until(lambda x: x.find_element(By.XPATH, '//div'))  # lamda 表达式
print(element.get_attribute('class'))
