import configparser
import os

current_path = os.path.dirname(__file__)
cfgpath = os.path.join(current_path, 'config.ini')


class ConfigUitl:
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
    def get_Log_path(self):
        value = self.read_ini('default', 'excel_path')
        return value


config_U = ConfigUitl()
if __name__ == "__main__":
    vluas = config_U.get_excel_path
    print(vluas)
