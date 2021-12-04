# 多态： 指的是一类食物具有多种形态，多态的前提是必须要实现继承
# 多态性：指具有不同功能的函数可以使用相同的函数名
# txt文件--- 双击--- 打开查看txt内容
# exe程序--- 双击--- 安装软件
# mp4视频--- 双击--- 播放视频

from abc import ABCMeta, abstractmethod


class File(metaclass=ABCMeta):  # 抽象父类
    @abstractmethod
    def Double_click(self):  # 抽象方法
        pass


# 实现多态
class txtFile(File):
    def Double_click(self):
        print('打开TXT文件查看内容')


class exeFile(File):
    def Double_click(self):
        print('打开exe安装软件')


class mp4File(File):
    def Double_click(self):
        print('打开mpe4播放内容')


# 实现多态性
def double_clicK(file_obj):
    file_obj.Double_click()


txt = txtFile()
exe = exeFile()
mp4 = mp4File()

# 调用实现多态性
double_clicK(txt)
double_clicK(exe)
double_clicK(mp4)
