# 系统默认自带的属性

class people:
    '''文档说明：我是people'''
    name = '无名氏'

    # 类中的构造方法
    def __init__(self, name, age):
        self.name = name
        self.age = age


# 访问内置属性： 类名.内置属性
print(people.__dict__)  # 打印出类的所有属性
print(people.__doc__)  # 类的文档字符串，只能放在类中第一行
print(people.__name__)  # 返回类名
print(people.__module__)  # 类定义所在的模块（运行的主函数）
print(people.__bases__)  # 所有类的父类都是object

