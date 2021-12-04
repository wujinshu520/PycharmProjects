import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

current = os.path.dirname(__file__)
chrome_dirver_path = os.path.join(current, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_dirver_path)
driver.implicitly_wait(10)
driver.get("http://www.baidu.com/")
# js_str1 ='alert("hello!!");'
# driver.execute_script(js_str1)
# 自动化常用js
# js_str2 = 'document.body.scrollTop=10000;'  # 浏览器滚动下滑操作js代码与浏览器兼容性
# driver.execute_script(js_str2)

# 上下滚动的操作
# js_str3 = 'document.body.scrollTop=%d;'
# for i in range(10):
#     if i % 2 == 0:
#         driver.execute_script(js_str3%10000)
#     else:
#         driver.execute_script(js_str3%-5000)

# 为了判断是否识别到一个元素，一般  获取元素的属性，操作元素
e = driver.find_element(By.XPATH, '//input[@id="kw"]')
# js_str4 = "kw.style.border= '5px solid red';"
# driver.execute_script(js_str4, e)
driver.execute_script("kw.style.border= '5px dashed #FFCCFF'", e)

# 移除属性
# js_str5 = "kw.removeAttribute('value');"
# driver.execute_script(js_str5,e)

# 修改属性
js_str6 = "var user_input = document.getElmentById('su').getAttribute('id');return user_input"
value = driver.execute_script(js_str6)
print(value)
