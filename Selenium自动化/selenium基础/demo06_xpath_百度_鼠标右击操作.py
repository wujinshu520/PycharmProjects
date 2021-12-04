import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get("https://www.baidu.com")
time.sleep(3)
#
# element = driver.find_element(By.XPATH,'//a[@name="tj_briicon"]')
# ActionChains(driver).move_to_element(element).perform()
# time.sleep(3)
# driver.find_element(By.XPATH,'//a[@name="tj_zhidao"]').click()

element = driver.find_element(By.XPATH,'//a[@href ="http://news.baidu.com"]')
ActionChains(driver).click_and_hold(element).pause(10).release(element).perform()