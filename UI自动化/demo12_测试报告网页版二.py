import time
import unittest
from HTMLTestRunner import HTMLTestRunner

class testCase(unittest.TestCase):
    def setUp(self) -> None:
        print("初始化")

    def tearDown(self) -> None:
        print("测试后的清理")

    def test_case_01(self):
        """加法运行的第一条用例"""
        self.assertEqual(1 + 3, 4)
        print("测试用例 test_case_01 执行完毕")

    def test_case_02(self):
        """加法运行的第二条用例"""
        self.assertEqual(2 + 3, 5)
        print("测试用例 test_case_02 执行完毕")

    def test_case_03(self):
        """加法运行的第三条用例"""
        self.assertEqual(3 + 3, 6)
        print("测试用例 test_case_03 执行完毕")


if __name__ == "__main__":
    # unittest.main()
    # unittest.main(verbosity=2)
    suite = unittest.TestSuite()
    suite.addTest(testCase("test_case_03"))
    suite.addTest(testCase("test_case_02"))
    suite.addTest(testCase("test_case_01"))
    new_time = time.strftime("%Y-%m-%d %H:%M:%S")
    # file = open('test_result' + new_time + '.html', 'wb')
    file = open('test_result%s.html'%new_time, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=file,
                                           title="new测试",
                                           description="测试用例执行报告")
    runner.run(suite)
    file.flush()
    file.close()
