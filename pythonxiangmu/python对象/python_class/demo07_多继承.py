# 多继承： 一个子类有多个父亲
# 人类-- 老师-- 司机

class people:  # 父类
    def __init__(self, name):
        self.name = name

    def say(self):
        print('我是一个人类')

    def run(self):
        print('我会跑步！！！')


class teacher:  # 父类
    def __init__(self, courseName):
        self.courseName = courseName

    def say(self):
        print('我是一个老师')

    def sleep(self):
        print('我是老师，我需要睡觉')


class driver(people, teacher):  # 子类，有2个父类，老师晚上兼职跑滴滴当兼职司机

    # 实现多个父类的构造方法
    def __init__(self, name, courseName, carbrand):
        people.__init__(self, name)
        teacher.__init__(self, courseName)
        self.carbrand = carbrand

    def speed_up(self):
        print('加速冲！！！！')

    # 多继承中假如父类有同名的方法，那么就按照继承的现货顺序来取
    def say(self):
        print('我是一个兼职的滴滴司机')


zhangyi = driver('张一', '女', 'GTR')
print(zhangyi.name)
print(zhangyi.carbrand)
print(zhangyi.courseName)
print('----------------------')
zhangyi.say()
zhangyi.run()   #  people
zhangyi.sleep()  # teacher
zhangyi.speed_up()