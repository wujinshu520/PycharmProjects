# 继承：一个类获取另外一个类的属性和方法的过程
#  子类获取父类的属性或者方法
# 人类：属性 name、age、sex 方法：say()  sleep()
# 学生：属性 name、age、sex、studengtid 、score 方法：say()  sleep()  studey()

class people:  # 父类

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def say(self):
        print('我是一个正直的人！！！！！')

    def sleep(self):
        print('我每天都需要睡觉休息！！！！')

    # 私有的属性和方法是不能被继承的
    def __DriverCar(self):
        print('我是一个车神，我开86，秋名山见')


class student(people):  # 子类  继承于people
    # 父类有构造方法的话，那么必须实现构造方法
    def __init__(self, name, age, sex, studentid):
        # 方法1：调用父类的构造方法,必须要传self
        # people.__init__(self,name, age, sex)

        # 方法2：使用super(),不需要传self
        # super().__init__(name, age, sex)

        # 方法3： 使用super()，此时第一个参数要写子类的名称
        super(student, self).__init__(name, age, sex)
        self.studentid = studentid

    def study(self):
        print('我是学生，我要好好学习！！')

    # 子类重写父类方法，当父类和子类有同名方法时，那么会先从自身类中开始调用
    def DriverCary(self):
        print('我也是一个车神，我开GTR')

    # 子类中的方法和父类重名（重写父类方法），那么子类调用的时候会先调用自己的
    def say(self):
        print('我是一个学生，我也会说话！！！')


lisi = people('李四', 20, '男')
lisi.say()
print(lisi.name)

print('----------------------------')

zs = student('张三', 20, '男', 10)
zs.study()
print(zs.name)
zs.DriverCary()
zs.say()
print('----------------------------')

print('张三的个人信息：', zs.name, zs.age, zs.sex, zs.studentid)
