import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.get("https://www.baidu.com")
time.sleep(3)

# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(Keys.TAB)
# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys('12306')
# time.sleep(3)
# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(Keys.BACKSPACE)

# 网页上的键盘操作
# driver.find_element(By.XPATH, '//input[@id="kw"]').send_keys(Keys.TAB)
# time.sleep(3)
# ActionChains(driver).send_keys(Keys.TAB).perform()

# 实战；
# element =driver.find_element(By.XPATH, '//input[@id="kw"]')
# ActionChains(driver).click(element)\
#         .pause(1).send_keys(Keys.TAB)\
#         .pause(1).send_keys(Keys.TAB)\
#         .pause(1).send_keys(Keys.TAB)\
#         .pause(1).send_keys(Keys.ENTER)\
#         .perform()
#
# # macOS 弱项
# driver.find_element(By.XPATH,'//input[@id="kw"]').send_keys(Keys.CONTROL,'V')

# Ctrl+V  按下Ctrl不放 -- 按下V键---松开V键----松开Ctrl键
element = driver.find_element(By.XPATH,'//input[@id="kw"]').click()
time.sleep(1)
ActionChains(driver).click(element).pause(1)\
        .key_down(Keys.CONTROL)\
        .send_keys('v').key_up(Keys.CONTROL).perform()

# selenium 里面修饰健  用key_down、 key_up、Ctrl、shirt、ait


# ALT+ F4  CTRL+ALT+DELETE  组合键==》 操作系统级别的快捷键
ActionChains(driver).key_down(Keys.ALT)\
        .send_keys(Keys.F4)\
        .key_up(Keys.ALT).perform()



