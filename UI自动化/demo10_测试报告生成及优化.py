import unittest


class testCase(unittest.TestCase):
    def setUp(self) -> None:
        print("初始化")

    def tearDown(self) -> None:
        print("测试后的清理")

    def test_case_01(self):
        self.assertEqual(1 + 3, 4)
        print("测试用例 test_case_01 执行完毕")

    def test_case_02(self):
        self.assertEqual(2 + 3, 5)
        print("测试用例 test_case_02 执行完毕")

    def test_case_03(self):
        self.assertEqual(3 + 3, 6)
        print("测试用例 test_case_03 执行完毕")


if __name__ == "__main__":
    # unittest.main()
    # unittest.main(verbosity=2)
    suite01 = unittest.TestSuite()
    suite01.addTest(testCase("test_case_03"))
    suite01.addTest(testCase("test_case_02"))
    suite01.addTest(testCase("test_case_01"))
    # unittest.main(defaultTest="suite01")
    # TextTestrunner 执行测试用例集
    # test_run = unittest.TextTestRunner(stream=None,
    #                                    descriptions="测试",
    #                                    verbosity=2)
    # test_run.run(suite01)


    # 方式2
    with open("test_result.txt", 'w', encoding="utf-8") as file:
        runner = unittest.TextTestRunner(stream=file,
                                         descriptions="测试",
                                         verbosity=2)
        runner.run(suite01)


