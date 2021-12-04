import os
import time
import unittest

import xlwt
from selenium import webdriver
from selenium.webdriver.common.by import By
from HTMLTestRunner import HTMLTestRunner


class zapdao_Case(unittest.TestCase):
    def setUp(self):
        self.driver_currnt = os.path.dirname(__file__)
        self.chrome_dirver_path = os.path.join(self.driver_currnt, '../Selenium自动化/webdriver/chromedriver')
        self.driver = webdriver.Chrome(executable_path=self.chrome_dirver_path)
        self.driver.get("http://47.107.178.45/zentao/www/index.php?m=user&f=login")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)

    def tearDown(self):
        time.sleep(5)
        self.driver.quit()

    def test_login_01(self):
        self.driver.find_element(By.XPATH, '//input[@name="account"]').send_keys("test01")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("newdream123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        time.sleep(2)
        actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        # 断言
        self.assertEqual(actual_result, "测试人员1", "test_login_01用例测试失败")
        time.sleep(2)
        # self.driver.get_screenshot_as_file('20210911zandao.png')

    def test_login_02(self):
        self.driver.find_element(By.XPATH, '//input[@name="account"]').send_keys("test02")
        self.driver.find_element(By.XPATH, '//input[@name="password"]').send_keys("newdream123")
        time.sleep(2)
        self.driver.find_element(By.XPATH, '//button[@id="submit"]').click()
        time.sleep(2)
        actual_result = self.driver.find_element(By.XPATH, '//span[@class="user-name"]').text
        # 断言
        self.assertEqual(actual_result, "测试人员2", "test_login_02用例测试失败")
        time.sleep(2)


if __name__ == "__main__":
    suite = unittest.TestSuite(unittest.makeSuite(zapdao_Case))
    new_time = time.strftime("%Y-%m-%d %H:%M:%S")
    file = open('test_result%s.html' % new_time, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title="new测试",
                                           description="测试用例执行报告")
    runner.run(suite)
    file.flush()
    file.close()
