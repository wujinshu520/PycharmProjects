# 内置方法

class people:
    # 1、构造方法:支持重载，但是系统会调用最后一个
    # 有构造方法的话系统会默认调用构造方法
    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def __init__(self, name, age):
        self.name = name
        self.age = age

    # 2、析构方法：释放资源
    def __del__(self):
        print('我是析构方法，在程序运行完之后会自动释放资源')

    # 3、 自定义实例输出方法
    def __str__(self):
        return '我是实例默认输出的内容'

    # 4、两个实例的加法操作（指对象的属性值相加）
    def __add__(self, other):
        return self.age + other.age


zhangsan = people('张三', 20)
lisi = people('李四', 19)
# del zhangsan  # 手动释放对象
print('---------------------')
print(zhangsan)
print(lisi)
print(zhangsan+lisi)
print(zhangsan.age+lisi.age)

