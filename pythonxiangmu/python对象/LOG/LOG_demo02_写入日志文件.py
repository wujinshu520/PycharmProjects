'''
日志级别：
1、DEBUG
2、INFO
3、WARNING
4、ERROR
5、CRITICAL
'''

import logging
import os
import loguru

# 创建日志对象
logger = logging.getLogger('python实战日志')
logger.setLevel(level=logging.INFO)

console = logging.StreamHandler()  # 创建一个控制台输出对象
formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
console.setFormatter(formatter)  # 使用日志格式
console.setLevel(level=logging.ERROR)  # 自定义日志级别  设定的级别 error 过滤掉error 过滤以下级别的日志


# 获取写入日志文件的路径
current_path = os.path.dirname(__file__)
log_path = os.path.join(current_path, 'python.log')
print(log_path)

# 创建一个文件类型的日志对象
file_log = logging.FileHandler(log_path, encoding='utf-8')
formatter = logging.Formatter('file:%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
file_log.setFormatter(formatter)


logger.addHandler(console)   # 日志对象配置在控制台输出
logger.addHandler(file_log)   # 日志对象写入到文件中输出现在

logger.error('天天向上！！！')
logger.info('好好学习!!!!')
