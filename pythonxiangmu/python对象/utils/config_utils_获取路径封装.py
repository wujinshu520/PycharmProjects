import configparser
import os

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, '../utils/config.ini')


class Config_Utils:
    def __init__(self, config_path=cfgpath):
        self.config_path = config_path
        self.conf = configparser.ConfigParser()
        self.conf.read(self.config_path, encoding="utf-8")

    def read_ini(self, sec, option):
        value = self.conf.get(sec, option)
        return value

    def get_excel_path(self):
        value =self.read_ini('default', 'excel_path')
        return value


if __name__ == '__main__':
    config_u = Config_Utils()
    print(config_u.get_excel_path())