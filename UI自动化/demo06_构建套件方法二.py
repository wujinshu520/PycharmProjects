import unittest


class TestDome_01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_login_case06_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_login_case06_01")

    def test_login_case06_02(self):
        self.assertEqual(2 + 3, 5)
        print("exec test_login_case06_02")

    def test_login_case06_03(self):
        self.assertEqual(3 + 3, 6)
        print("exec test_login_case06_03")


class TestDome_02(unittest.TestCase):
    def test_login_case06_02_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_login_case02_01")


if __name__ == "__main__":
    # 构建套件方式二： 使用makeSuite() 加载整个测试类的用例
    testSuite = unittest.TestSuite(unittest.makeSuite(TestDome_01))
    unittest.main(defaultTest="testSuite")

