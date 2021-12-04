import configparser
import os

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, '../utils/config.ini')


class Config_Utils:
    def __init__(self, config_path=cfgpath):
        self.__conf = configparser.ConfigParser()
        self.__conf.read(config_path, encoding="utf-8")

    def read_ini(self, sec, option):
        value = self.__conf.get(sec, option)
        return value

    @property
    def get_excel_path(self):
        value = self.read_ini('default', 'excel_path')
        return value

    @property
    def get_log_path(self):
        value = self.read_ini('default', 'log_path')
        return value

    @property
    def get_email_username(self):
        value = self.read_ini('email', 'user_name')
        return value


Config = Config_Utils()

if __name__ == '__main__':
    config_u = Config_Utils()
    print(config_u.get_excel_path)
