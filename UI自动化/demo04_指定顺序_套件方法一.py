import unittest


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_ccc(self):
        print("订单商品已发出")
        print("测试用例ccc执行完毕")

    def test_bbb(self):
        print("订单已支付")
        print("测试用例bbb执行完毕")

    def test_aaa(self):
        print("购物车中的商品已下单")
        print("测试用例aaa执行完毕")


if __name__ == "__main__":
    # 方式1： addTest()方式加载用例
    suite = unittest.TestSuite()  # 新建测试套件
    suite.addTest(TestCase('test_ccc'))  # 加载测试用例
    suite.addTest(TestCase('test_aaa'))
    unittest.main(defaultTest='suite')
