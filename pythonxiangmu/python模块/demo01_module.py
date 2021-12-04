# 模块： 一个.py文件就是一个模块

'''
# 1、内置模块： sys、os、time  系统自带的
# print(help('modules'))  # 查看系统的内置模块
# 2、自定义模块（自己编写的），不能和python自带的模块名称冲突
# 3、开源的模块（第三方模块）

# 导入模块
# import 模块名称
import sys, time
print('---------1--------')
time.sleep(3)
print('---------2--------')

# 2、from 包名.模块名称 import 方法名称【常用】
# from pythonxiangmu.python模块.testa import pri,add,say  # 导入单个方法
from pythonxiangmu.python模块.testa import *   # 导入所有的方法
from pythonxiangmu.python模块.test.testb import *

# 给方法取别名，取别名之后之前的方法名称就不能在使用了
from pythonxiangmu.python模块.testa import pri as bie_pri  # 导入所有的方法
# 导包的顺序是从上往下
bie_pri()
#
pri()
'''

# 3、导入整个模块
from python.python模块 import testa
testa.pri()
