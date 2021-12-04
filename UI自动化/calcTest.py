# 计算器测试类
import unittest

from python.UI自动化.calc import *


class Mytest(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sum_case01(self):
        self.assertEqual(add(2, 3), 5, '加法计算失败')

    def test_sum_case02(self):
        self.assertEqual(add(2, 3), 4, '加法计算失败')

    def test_sub_case01(self):
        self.assertEqual(sub(10, 5), 5, '减法测试失败')

    def test_sub_case02(self):
        self.assertEqual(sub(10, 5), 3, '减法测试失败')


if __name__ == "__main__":
    unittest.main()

