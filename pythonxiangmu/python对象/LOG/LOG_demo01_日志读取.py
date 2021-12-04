'''
日志级别：
1、DEBUG 2、INFO 3、WARNING 4、ERROR 5、CRITICAL
'''
import logging

logger = logging.getLogger('python实战日志') # 创建日志对象
logger.setLevel(level=logging.INFO)  # 设置全局日志级别

# 在控制台打印日志
console = logging.StreamHandler()  # 创建一个控制台输出对象

# 设置日志格式
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
console.setFormatter(formatter)  # 使用日志格式
logger.addHandler(console)  # 日志对象配置在控制台输出
logger.info('今天好好学习')

