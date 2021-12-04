import unittest
import os

# 获取当前run_allCase文件的所在目录
corren_path = os.path.dirname(__file__)
print(corren_path)

# 用例目录
start_path = os.path.join(corren_path, 'test_one')
print(start_path)

# discover的作用：搜索满足规则的用例
discover = unittest.defaultTestLoader.discover(start_path,  # 要测试的模块名或者测试用例目录
                                               pattern='test*.py',  # 表示用例文件名的匹配原则
                                               top_level_dir=start_path)  # 测试模块的顶层目录
mainSuite = unittest.TestSuite()
mainSuite.addTests(discover)  # 把discover搜索处理的用例加载到套件中
unittest.main(defaultTest="mainSuite")
