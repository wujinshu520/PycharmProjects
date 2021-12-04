import unittest


class testCase_02(unittest.TestCase):
    def setUp(self) -> None:
        print("初始化")

    def tearDown(self) -> None:
        print("测试后的清除")

    def test_1(self):
        self.assertEqual(5, 2 + 3, '检查加法')
        print('Equal 断言执行结束')

    def test_2(self):
        self.assertNotEqual(1 + 2, 2)  # 不等于测试通过
        print("Not Equal 断言执行结束")

    def test_3(self):
        a = 1 == 1  # a 为真
        self.assertTrue(a, "判断为真-失败")
        print("True 执行结束")

    def test_4(self):
        a = 1 == 2  # a 为真
        self.assertTrue(a, "判断为真-失败")
        print("test_4 执行结束")

    def test_5(self):
        city_list = ['上海', '北京', '杭州', '深圳']
        self.assertIn('上海', city_list, '元素不在集合中')
        print('In 断言执行结束')

    def test_6(self):
        city_list = ['上海', '北京', '杭州', '深圳']
        city_list2 = city_list
        city_list3 = city_list[:]
        print(id(city_list))
        print(id(city_list2))
        print(id(city_list3))
        self.assertIs(city_list2, city_list, '不是同一个对象')
        print('In 断言执行结束')
        self.assertIs(city_list3, city_list, '是同一个对象')
        print('In 断言执行结束')

    def test_7(self):  # 类型判断
        name = 'wujinshu'
        self.assertIsInstance(name,str,'类型判断失败')
        print('IsInstance 断言执行结束')



if __name__ == "__main__":
    unittest.main()
