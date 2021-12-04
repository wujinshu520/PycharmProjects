# 属性（类属性，实例属性，内置属性）
# 方法（类方法、实例方法、静态方法）

class cat:
    name = '无名氏'  # 类属性
    age = None

    def __init__(self, my_name, sex, age):
        self.my_name = my_name  # 实例属性
        self.sex = sex
        self.__age = age # 私有属性，只能内部使用，不能外部调用

    # 实例方法（类当中的普通方法）
    def sleep(self):
        print('我是一个喵喵喵，我喜欢睡觉！')

    def say(self):
        print('我是一只喵喵喵!!!!')

    @classmethod  # 修饰器：它下面的方法就是类方法
    def run(cls):  # 类方法的第一个参数默认是cls
        print('我是一个类方法')

    @staticmethod  # 它下面的方法就是静态方法
    def static():  # 静态方法不需要多定义参数
        print('我是一个静态方法')


tom = cat('汤姆', '公',5)

# 1、通过（对象、类名） 访问类属性
print(tom.name)
print(cat.name)

# 2、通过对象访问实例属性
print(tom.my_name)

# 3、通过对象、类名  访问内置属性
print(tom.__dict__)
print(cat.__module__)

# 4、 通过 对象、类名  访问类方法
tom.run()
cat.run()

# 5、# 通过 对象、类名  访问静态方法
tom.static()
cat.static()

# 6、 通过 对象、类名  访问实例方法
tom.say()

# 通过 类名 访问实例方法，那么该方法会被当作普通方法，self需要传参
cat.say('tt')

