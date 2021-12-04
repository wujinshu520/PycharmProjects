import unittest


class Test_Case(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_sum_case01(self):
        self.assertEqual(1 + 2, 3)

    @unittest.skip("无条件跳过")
    def test_sum_case02(self):
        self.assertEqual(1 + 2, 2)

    @unittest.skipIf(True, "条件为真跳过")
    def test_sum_case03(self):
        self.assertEqual(1 + 2, 3)

    @unittest.skipUnless(False, "条件为假跳过")
    def test_sum_case04(self):
        self.assertEqual(1 + 4, 4)

    @unittest.expectedFailure  # 失败不计入失败的数量中
    def test_sum_case05(self):
        self.assertEqual(1 + 2, 2)


if __name__ == "__main__":
    unittest.main()
