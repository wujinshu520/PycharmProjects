import unittest  # 步骤1：导入unittest模块


class TestDemo(unittest.TestCase):  # 步骤2：继续TestCase
    def setUp(self):  # 方法预期的返回值类型为None 非强制
        print('前置条件')  # 步骤3

    def tearDown(self):
        print('测试后的清除')

    def test_add(self):  # 步骤4 ：编写test打头的测试用例
        self.assertEqual(10 + 6, 16, 'test_add 执行成功')  # 步骤5： 断言
        print('test_add')


if __name__ == "__main__": # 步骤6：执行脚本
    unittest.main()
