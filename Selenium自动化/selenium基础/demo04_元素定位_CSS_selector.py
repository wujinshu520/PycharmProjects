# 获取驱动路径
import os
import time

from selenium import webdriver
from selenium.webdriver.common.by import By

courrent = os.path.dirname(__file__)
chrome_driver_path = os.path.join(courrent, '../webdriver/chromedriver')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.baidu.com")

''' 绝对路径 
id 用 #、 class 用 .
'''
#  driver.find_element_by_css_selector('html body div#wrapper div#head div#head_wrapper div div form span.bg.s_ipt_wr.quickdelete-wrap input').send_keys('新闻')

'''相对路径 自底向上 '''
# driver.find_element_by_css_selector('input#kw').send_keys('新闻')
# driver.find_element_by_css_selector('span.bg.s_ipt_wr.quickdelete-wrap input#kw').send_keys('新闻')

''' 属性定位 '''
# driver.find_element_by_css_selector('input[maxlength="255"]').send_keys("新闻")

''' 多属性定位  只支持 and的效果'''
# driver.find_element_by_css_selector('input[maxlength="255"][id="kw"]').send_keys("新闻")

''' 模糊属性定位 称为部分属性值定位  '''
# ^= 以什么属性内容开头
# driver.find_element_by_css_selector('a[href^="http://news"]').click()

# $= 以什么属性内容结尾
# driver.find_element_by_css_selector('a[href$="news.baidu.com"]').click()

# *= 包含什么属性内容
# driver.find_element_by_css_selector('a[href*="news.baidu.com"]').click()

'''   查询子元素    '''
# 子元素 A>B
# driver.find_element_by_css_selector('form>span>input').send_keys("英雄联盟")

# 后代元素 A空格B（类似>）
# driver.find_element_by_css_selector('form span input').send_keys("英雄联盟")

# 第一个后代元素 ： first-child
# driver.find_element(By.CSS_SELECTOR, 'div#s-top-left a:first-child').click()
# driver.find_element_by_css_selector('div#s-top-left a:first-child').click()


# 最后一个后代元素 ：last-child
# driver.find_element(By.CSS_SELECTOR, 'div#s-top-left a:last-child')
# driver.find_element_by_css_selector('div#s-top-left a:last-child').click()

# 第n个子元素
# driver.find_element_by_css_selector('div#s-top-left a:nth-child(4)').click()
# driver.find_element_by_css_selector('div#s-top-left a:nth-of-type(4)').click()

# 兄弟元素 +
# driver.find_element_by_css_selector('div#s-top-left a +a +a +a').click()

# 选择同层级多个相同标签的元素
# es = driver.find_element_by_css_selector('div#s-top-left a ~a')
# es.click()
# print(type(es))

''' 新的定位语法 更适合用在框架 '''
# driver.find_element(By.ID, 'kw').send_keys('英雄联盟')
driver.find_element(By.XPATH, '//input[@id ="kw"]').send_keys('英雄联盟')

time.sleep(10)
# 关闭当前浏览器
driver.quit()
