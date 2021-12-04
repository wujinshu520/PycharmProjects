import unittest


class TestCase(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass

    def test_ccc(self):
        print("订单商品发出")
        print("测试用例ccc执行完毕")

    def test_bbb(self):
        print("订单已支付")
        print("测试用例bbb执行完毕")

    def test_aaa(self):
        print("购物车中的商品已下单")
        print("测试用例aaa执行完毕")


if __name__ == "__main__":
    # 1、默认名称顺序
    unittest.main()
