# 日志工具包

import logging
from python.pythonxiangmu.python对象.utils.config_utils_私有封装 import *

# current_path = os.path.dirname(__file__)
# log_path = os.path.join(current_path, '../LOG/python.log')
# print(log_path)


class LogUtils:
    def __init__(self, logfile_path=Config.get_log_path):
        self.logfile_path = logfile_path
        self.logger = logging.getLogger()
        self.logger.setLevel(level=logging.INFO)

        # 创建一个文件类型的日志对象
        file_log = logging.FileHandler(Config.get_log_path, encoding='utf-8')
        formatter = logging.Formatter('%(asctime)s - %(filename)s[line:%(lineno)d] - %(levelname)s: %(message)s')
        file_log.setFormatter(formatter)
        file_log.setLevel(level=logging.INFO)  # 注意单独的日志级别必须要比全局的优先级要高才能有作用
        self.logger.addHandler(file_log)

    def info(self, message):  # 写入正常的日志信息
        self.logger.info(message)

    def error(self, message):  # 写入错误的日志信息
        self.logger.error(message)


logger = LogUtils()

if __name__ == '__main__':
    Log_Utils = LogUtils()
    Log_Utils.error('错误咯！！')
