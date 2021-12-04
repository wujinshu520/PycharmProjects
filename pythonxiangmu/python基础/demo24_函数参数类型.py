# 函数参数类型：必备参数，关键字参数，缺省参数，任意个数参数
# 1、必备参数:传递的顺序和个数都是不能变的
def info1(name, age):
    print('我的名字是{},我的年龄是{}'.format(name, age))


info1('吴进书', 23)
print('----------------------')


# 2、关键字参数：参数列表顺序是可以改变的
def info2(name, age):
    print('我的名字是{},我的年龄是{}'.format(name, age))


info2(age=23, name='吴进书')
print('----------------------')


# 3、缺省参数：为传参的参数必须要有默认值
def info3(name, age=20):
    print('我的名字是{},我的年龄是{}'.format(name, age))


info3(name='吴进书')
print('----------------------')


# 4、任意个数参数：在重复调用函数时默认形参（可变数据类型）会继承之前一次调用结束之后该行参的值
def pri(a, listb=[]):
    listb.append(a)
    print(listb)


pri(1)
pri(2)
print('----------------------')


# 5、收集参数（不定长参数）：当需要一个函数能处理比当初声明时更多的参数
# * 和 ** 表示能够接受0到任意个参数
# * 表示将没有匹配到的值都放到同一个元组中
def pri2(name, *test_tuple):
    print(name)
    print(test_tuple, type(test_tuple))


pri2('张三', 20, '测试', 1, 2, 3, )
print('----------------------')


# ** 表示将没有匹配到的值都放到同一个字典中
def pri3(name, **test_dict):  # 多余参数必须是键值对： key=value 的格式
    print(name)
    print(test_dict, type(test_dict))


pri3('李四', age=20, test_name='张三')
