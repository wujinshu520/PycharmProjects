import unittest
import demo06_构建套件方法二


class TestDome_01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_login_case07_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_login_case07_01")

    def test_login_case07_02(self):
        self.assertEqual(2 + 3, 5)
        print("exec test_login_case07_02")

    def test_login_case07_03(self):
        self.assertEqual(3 + 3, 6)
        print("exec test_login_case07_03")


class TestDome_02(unittest.TestCase):
    def test_login_case02_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_login_case02_01")


if __name__ == "__main__":
    # 构建套件方式三：
    # 1、加载测试类里面的所有用例
    # suite01 = unittest.TestLoader().loadTestsFromTestCase(TestDome_01)
    # unittest.main(defaultTest="suite01")

    # 2、加载模版py文件里面的测试用例 # 注意：需要导入testCase 这个模块
    # suite02 = unittest.TestLoader().loadTestsFromModule(demo06_构建套件方法二)
    # unittest.main(defaultTest="suite02")

    # 使用字符串的方式加载
    # 3.1 加载测试方法
    suite03 = unittest.TestLoader().loadTestsFromName("demo07_构建套件方法三.TestDome_01.test_login_case_01")

    # 3.2 加载测试类
    suite04 = unittest.TestLoader().loadTestsFromName("demo07_构建套件方法三.TestDome_02")

    # 3.3 加载模块
    suite05 = unittest.TestLoader().loadTestsFromName("demo07_构建套件方法三")
    unittest.main(defaultTest="suite05")
