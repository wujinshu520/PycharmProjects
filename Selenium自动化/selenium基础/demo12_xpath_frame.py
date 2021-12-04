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
driver.switch_to_frame("frame1") # 方法目前还可用，但是已有新方法
frame_element = driver.find_element(By.XPATH,'//iframe')
driver.switch_to_frame(frame_element) # 跳进去
driver.find_element(By.XPATH,'//input[@id ="input1"]').send_keys('newdream')
driver.find_element(By.XPATH,'//body/input[2]').send_keys('holle')
driver.switch_to.default_content() # 跳转到主框架页面
value = driver.find_element(By.XPATH,'//div[@id="id1"]').text
print(value)
