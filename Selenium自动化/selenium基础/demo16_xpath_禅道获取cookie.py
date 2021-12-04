import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(10)
driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")

# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)
#
# cookie_value = driver.get_cookies('theme')
# print(cookie_value)


'''方式一： 浏览器获取cookie'''
# driver.add_cookie({'domain': '47.107.178.45', 'name': 'zentaosid', 'path': '/', 'value': 'pr7k4822palh558u0kp05bg296'})
# driver.add_cookie({'domain': '47.107.178.45', 'expiry': 1632835143, 'name': 'theme', 'path': '/zentao/www/', 'value': 'default'})
# driver.add_cookie({'domain': '47.107.178.45', 'name': 'windowHeight', 'path': '/zentao/www', 'value': '644'})
# driver.add_cookie({'domain': '47.107.178.45', 'name': 'windowWidth', 'path': '/zentao/www', 'value': '1200'})
# driver.add_cookie({'domain': '47.107.178.45', 'expiry': 1632835143, 'name': 'device', 'path': '/zentao/www/', 'value': 'desktop'})
# driver.add_cookie({'domain': '47.107.178.45', 'expiry': 1632835143, 'name': 'lang', 'path': '/zentao/www/', 'value': 'zh-cn'})
# time.sleep(3)
# driver.refresh()

'''方式二；打开验证码页面---等待30s----手工输入用户名、密码、验证码、点击提交或登录---打印所有的cookie'''
# time.sleep(30)
# cookies = driver.get_cookies()
# for cookie in cookies:
#     print(cookie)
driver.add_cookie({'domain': '47.107.178.45','name': 'zentaosid', 'path': '/',  'value': 'ruv3d95ug19ilto0dvpseo32m2'})
driver.add_cookie({'domain': '47.107.178.45', 'name': 'windowHeight', 'path': '/zentao/www', 'value': '641'})
driver.add_cookie({'domain': '47.107.178.45',  'name': 'ajax_lastNext', 'path': '/zentao/www/','value': 'on'})
driver.add_cookie({'domain': '47.107.178.45', 'name': 'theme', 'path': '/zentao/www/','value': 'default'})
driver.add_cookie({'domain': '47.107.178.45',  'name': 'windowWidth', 'path': '/zentao/www', 'value': '1200'})
driver.add_cookie({'domain': '47.107.178.45', 'name': 'device', 'path': '/zentao/www/', 'value': 'desktop'})
driver.add_cookie({'domain': '47.107.178.45', 'name': 'lang', 'path': '/zentao/www/',  'value': 'zh-cn'})
time.sleep(3)
driver.refresh()


