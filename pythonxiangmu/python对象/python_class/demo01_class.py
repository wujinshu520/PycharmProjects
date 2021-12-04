# 对象：某个类中具体的一个实例（属性、方法）
'''
int a; # 先定义后赋值
a = 5;

int a= 5； # 直接定义赋值-->初始化赋值

'''


class people:  # class 类名称
    name = '无名氏'  # 类属性
    age = None
    sex = None

    # 构造方法：完成对象的初始化，在创建对象的时候系统会默认调用构造方法
    def __init__(self, name, age, sex,address):
        self.name = name  # 实例属性
        self.age = age
        self.sex = sex
        self.address =address

    # 类中的方法
    def say(self):  # 类中的方法会自带self，表示当前类的所有属性和方法
        print('我是一个爱好劳动，爱好生活的人')

    def eat(self):
        print('我喜欢吃美食')


tom = people('张一',5,'男','上海')  # 创建对象--> 对象名称= 类名()
# tom.name = '张一'
# tom.age = 24
# print(tom.name)  # 调用对象的属性、方法-> 对象名.属性或者方法
tom.say()
tom.eat()
print('我的名字叫：{},我今年{}岁'.format(tom.name, tom.age))
