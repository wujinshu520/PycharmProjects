# 抽象类
'''

1、抽象类中要有抽象方法
2、要有抽象类的定义语句
3、抽象类是用来被继承的，如果没有被继承那么毫无意义

'''

from abc import abstractmethod, ABCMeta


class animal(metaclass=ABCMeta):  # 也是定义抽象类，强制必须实现父类的抽象方法
    # 定义抽象类  此写法不是强制性必须实现父类的抽象方法
    # __metaclass__ = ABCMeta

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 抽象方法: 只定义不实现具体的内容，子类必须实现父类的抽象方法
    @abstractmethod
    def say(self):
        pass


class dog(animal):
    # 父类是抽象类
    # 1、父类是抽象方法
    # 2、子类本身也是抽象类
    def __init__(self, name, age):
        super(dog, self).__init__(name, age)

    def say(self):
        print('我是子类，我必须实现父类的抽象方法!!!!')


xiaohuang = dog('小黄', 2)
xiaohuang.say()
