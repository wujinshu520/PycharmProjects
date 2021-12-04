# pythonxiangmu 中在导入模块的时候会立即
import sys
from python.python模块.test.a import pri, pri2

pri()
pri2()

# b 模块中的__main__
print('环境变量：', sys.path)
