import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
page_path = os.path.join(current, '../page_path/wait.html')

driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(20)  # 隐示等待
driver.get('file://' + page_path)
driver.find_element(By.XPATH, '//button').click()
# time.sleep(5)  # 固定等待
value = driver.find_element(By.XPATH, '//div').get_attribute('class')
print(value)

# 智能等待：在一个时间段内的等待
#  implicitly_wait
#  1、全局设置 find_element 、find_elements
#  2、机制：每隔500ms在界面进行一次检查，如果检查到了就不等待，如果在设置的时间没有检查到那么才报错


