# 封装: 数据封装、方法封装

class people:
    def __init__(self, name, money):
        self.name = name

        # 私有属性，只能在类的内部使用--> 数据的封装
        # 数据的封装： 私有的属性，只能在类的内部使用，在类的外部访问不了
        self.__money = money

    # 方法的封装： 通过公有的方法来访问私有的属性
    def getMoney(self):  # 获取money的值
        return self.__money

    def __setMoney(self, money):  # 存钱  改变money的值
        self.__money = self.__money + money

    def run_setMoney(self, m):
        self.__setMoney(m)


zs = people('张三', 500)
print('张三的钱有：', zs.getMoney())

# 调用私有的方法一：
# zs.setMoney(200)
# print('张三存钱后有：',zs.getMoney())

# 调用私有的方法二： 封装调用方法后
zs.run_setMoney(100)
print('张三存钱后有：', zs.getMoney())

# 类的外部私有的属性、方法可以通过  对象._类名__私有属性、方法  的方式进行访问
zs._people__setMoney(50)
print(zs._people__money)