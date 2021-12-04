import time
from selenium import webdriver

courrent = os.path.dirname(__file__)
chrome_driver_path = os.path.join(courrent, '../webdriver/chromedriver')

driver = webdriver.Chrome(executable_path=chrome_driver_path)
driver.get("https://www.baidu.com")

""" ----写法一-----  """
# id 定位
# driver.find_element_by_id("kw").send_keys("新梦想")

# name定位
# driver.find_element_by_name("wd").send_keys("新中国")

# class 定位
# driver.find_element_by_class_name("s_ipt").send_keys("新梦想")

# tag_name 定位  标签名  比如input 不推荐使用
# driver.find_element_by_tag_name("input").send_keys("新梦想")

# link.text  链接中的文件 <a>标签生效
# driver.find_element_by_link_text("新闻").click()

# partial_link_text 部分链接中的文本
# driver.find_element_by_partial_link_text("新").click()


""" ----写法二-----  """
from selenium.webdriver.common.by import By
# driver.find_element(By.ID,"kw").send_keys("新闻")
driver.find_element(By.NAME,"wd").send_keys("新梦想")
