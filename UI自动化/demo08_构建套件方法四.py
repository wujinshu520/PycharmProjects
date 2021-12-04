import unittest
import demo06_构建套件方法二


class TestDome_01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_login_case01_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_login_case01_01")

    def test_login_case01_02(self):
        self.assertEqual(2 + 3, 5)
        print("exec test_login_case01_02")

    def test_login_case01_03(self):
        self.assertEqual(3 + 3, 6)
        print("exec test_login_case01_03")


class TestDome_02(unittest.TestCase):
    def test_login_case02_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_login_case02_01")


if __name__ == "__main__":
    #  构建套件方式四：把子套件，合成大的主套件，使用addTests()
    allSuite = unittest.TestSuite()
    suite01 = unittest.TestLoader().loadTestsFromTestCase(TestDome_01)
    suite02 = unittest.TestLoader().loadTestsFromModule(demo06_构建套件方法二)
    suite03 = unittest.TestLoader().loadTestsFromName(
        "demo07_构建套件方法三.TestDome_01.test_login_case_01")
    suite04 = unittest.TestLoader().loadTestsFromName("demo07_构建套件方法三.TestDome_02")
    suite05 = unittest.TestLoader().loadTestsFromName("demo07_构建套件方法三")
    # 加载子套件
    allSuite.addTests(suite01)
    allSuite.addTests(suite02)
    allSuite.addTests(suite03)
    allSuite.addTests(suite04)
    allSuite.addTests(suite05)
    unittest.main(defaultTest="allSuite")
