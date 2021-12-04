import unittest


class test_two_01(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_two_01_01(self):
        self.assertEqual(1 + 2, 3)
        print("exec test_two_01_01")

    def test_two_01_02(self):
        self.assertEqual(2 + 3, 5)
        print("exec test_two_01_02")

    def test_two_01_03(self):
        self.assertEqual(3 + 3, 6)
        print("exec test_two_01_03")


