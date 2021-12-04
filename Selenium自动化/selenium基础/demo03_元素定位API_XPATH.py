import os
import time

from selenium import webdriver

courrent = os.path.dirname(__file__)
chrome_driver_path = os.path.join(courrent, '../webdriver/chromedriver')
driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.baidu.com")
time.sleep(3)

"""  绝对路径 // 遇到同层级多个元素用下标表示，下标从1开始  自顶向下写  """
# driver.find_element_by_xpath("/html/body/div[1]/div[1]/div[3]/div/div/form/span[1]/input").send_keys("新梦想")

"""  相对路径 // 经验 自底向上去尝试 """
# driver.find_element_by_xpath("//span[1]/input").send_keys("新梦想")
# driver.find_element_by_xpath("//form/span[1]/input").send_keys("新梦想")

""" 属性定位  具体格式：driver.find_element_by_xpath('//标签名[@属性="属性值"]')  """
# driver.find_element_by_xpath('//input[@maxlength = "255"]').send_keys("新闻")
# driver.find_element_by_xpath('//input[@id = "kw"]').send_keys("新闻")

# 多属性定位 支持 and or
# driver.find_element_by_xpath('//input[@id = "kw" and @maxlength = "255"]').send_keys("新闻")
# driver.find_element_by_xpath('//input[@id = "kw" or @maxlength = "255"]').send_keys("新闻")

# 支持通配符 *
# driver.find_element_by_xpath('//*[@* = "kw"]').send_keys("新闻")

# 模糊定位， 称为部分属性值定位
# starts-with() 字符串以特定值开头
# driver.find_element_by_xpath('//a[starts-with(@href,"http://news")]').click()

# ends-with() 是xpath语言2.0版本的函数  而xpath1.0版本的语言
# driver.find_element_by_xpath('//a[ends-with(@href,"news.baidu.com")]').click()

# 元素属性值结尾
# substring() 截取
# driver.find_element_by_xpath("//a[substring(@href,8)='news.baidu.com']").click()

# 包含 contains()
# driver.find_element_by_xpath("//a[contains(@href,'news.baidu.com')]").click()
# 应用：1、元素信息过长
#  2、动态属性的元素  订单 取第一个订单点击  order_001  order_002  order_003

""" 
元素文本定位 
link_text 只能用于 a 标签，局限性比较大
text() 
"""
# driver.find_element_by_xpath('//a[text()="新闻"]').click()
driver.find_element_by_xpath("//a[contains(text(),'新')]").click()

