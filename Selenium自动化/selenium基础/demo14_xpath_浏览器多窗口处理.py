import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(10)
driver.get("http://jtj.kaifeng.gov.cn/")

# 在操作系统中，该窗口会产生一个独立的句柄（随机的字符串值、数字和字母组成，每次打开一个新窗口，句柄会变化）
handle = driver.current_window_handle  # 获取当前窗口句柄
print('当前窗口句柄', handle)

element = driver.find_element(By.XPATH, '//a[@href="/news/14720.cshtml"]')
ActionChains(driver).click_and_hold(element).pause(3).release(element).perform()
time.sleep(2)

handles = driver.window_handles  # 获取当前窗口句柄
print('当前窗口句柄', handles)

'''方法一：'''
handles.remove(handle)
new_handle = handles[0]

'''方法二：'''
# for i in range(handles):
#     if i != handle:
#         new_handle = i

driver.switch_to.window(new_handle)  # 切换窗口
driver.find_element(By.XPATH,'//*[@target = "_blank"]').click()
driver.switch_to.window(handle)
driver.find_element(By.XPATH,'//*[@id="searchkw"]').send_keys("疫情防控责任大 校园消杀保安全 红豹救援队为开封市一职专进行全面消杀")

