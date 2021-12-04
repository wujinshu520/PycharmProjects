import os
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


def switch_window_by_title(title):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.title.__contains__(title):
            break


def switch_window_by_url(url):
    for handle in driver.window_handles:
        driver.switch_to.window(handle)
        if driver.title.__contains__(url):
            break


current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(10)
driver.get("http://jtj.kaifeng.gov.cn/")

element = driver.find_element(By.XPATH, '//a[@href="/news/14720.cshtml"]')
ActionChains(driver).click_and_hold(element).pause(3).release(element).perform()
time.sleep(2)
# switch_window_by_title('开封市教育体育网')
switch_window_by_url("http://jtj.kaifeng.gov.cn/")
driver.find_element(By.XPATH, '//a[text()= "脱贫攻坚"]').click()
