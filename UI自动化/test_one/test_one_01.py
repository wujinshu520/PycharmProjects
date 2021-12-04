import unittest


class test_one_01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_one_01_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_one_01_01")

    def test_one_01_02(self):
        self.assertEqual(2 + 3, 5)
        print("exec test_one_01_02")

    def test_one_01_03(self):
        self.assertEqual(3 + 3, 6)
        print("exec test_one_01_03")


