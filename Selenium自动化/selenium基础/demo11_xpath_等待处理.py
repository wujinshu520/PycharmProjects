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

# 定位一组对象
eles = driver.find_element(By.XPATH, '//input[@type="checbox"]')

for e in eles:
    time.sleep(1)
    e.click()
