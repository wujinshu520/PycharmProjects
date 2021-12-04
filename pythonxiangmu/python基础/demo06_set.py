# 集合 是一个无序不重复的序列
'''
特点：
1、无序，没有下标
2、数据是不能重复
3、可以存放多种数据类型
4、可变数据类型
'''

# 注意： 创建空集合必须使用set()，否则创建的是字典dict

set_name = set()
print(set_name, type(set_name))

set_test = {1, '张一', 90, True, '张三', 90, 9}
print(set_test)

# 增加元素
set_test.add('貂蝉')
print(set_test)

# 删除元素
set_test.remove(1)
print(set_test)

a = {1, 2, 3, 4, 5}
b = {4, 5, 6, 7, 8}
# 集合运算
print('a和b的差集：', a - b)  # 打印a中存在的，但b中不存在的元素
print('b和a的差集：', b - a)  # 打印b中存在的，但a中不存在的元素
print('a和b的并集：', b | a)  # 打印a和b中不重复的元素
print('a和b的交集：', a & b)  # 打印a和b中同时存在的元素
print('a和b中不同时存在的元素：', a ^ b)  # 打印a和b中同时不存在的元素

# in 判断是否在结合里面
print(50 in a)