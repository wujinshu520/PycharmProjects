# 学生--- 去教室读书
# 老师--- 去教室上课
# people: name , age   方法：goto_class
from abc import ABCMeta, abstractmethod, ABC


class people(metaclass=ABCMeta):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @abstractmethod
    def goto_class(self):
        pass


class student(people):
    def __init__(self, name, age, studentid):
        people.__init__(self, name, age)
        self.studentid = studentid

    # 开发忘记写goto_class方法
    def goto_class(self):
        print('我是学生，我在教室学号是：{}号'.format(self.studentid))


class teacher(people):
    def __init__(self, name, age, CourseName):
        people.__init__(self, name, age)
        self.CourseName = CourseName

    def goto_class(self):
        print('我是老师，我去教室上{}课'.format(self.CourseName))


lisi = student('李四', 10, 1)
zhangsan = teacher('张三', 23, '语文')
lisi.goto_class()
zhangsan.goto_class()


