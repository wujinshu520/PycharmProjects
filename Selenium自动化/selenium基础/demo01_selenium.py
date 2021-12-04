import os
import time
from selenium import webdriver
"""

打开百度方法一：
下载chromedriver驱动，再移动到/usr/local/bin 目录下

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')  


"""
'''  打开驱动，访问：百度方法二  '''
courrent = os.path.dirname(__file__)
chrome_driver_path = os.path.join(courrent, '../webdriver/chromedriver')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.baidu.com")

time.sleep(3)
driver.minimize_window()  # 最小化浏览器
time.sleep(3)
driver.maximize_window()  # 最大化浏览器
time.sleep(3)
# driver.set_window_size(200, 200)  # 获取浏览器宽高
# driver.back()
# time.sleep(1)
# driver.forward()
size = driver.get_window_size()
url = driver.current_url  # 获取浏览器URL地址
title = driver.title  # 获取当前网页标题
pagesource = driver.page_source  # 获取当前网页源代码
print(size)
print("获取浏览器URL地址:"+url)
print("获取当前网页标题:"+title)
print("获取当前网页源代码:"+pagesource)
# driver.get_screenshot_as_file(os.getcwd()+"/screen/screen.png")
# driver.close()  # 关闭当前Tab页签
driver.quit()  # 关闭当前浏览器
