# 元组tuple
'''
特点：
1、不能二次赋值
2、有下标
3、可以存放多种数据类型，可以重复
'''

name = ('小红', '小黄', '小蓝', '小红', True, 8.8)
print(name, type(name))
# name[1] = '西施'
# print(name)

# 重新赋值
list1 = [1, 2, 3]
list1[0] = '张三'
print(list1)

# 空元祖
tup1 = ()

# 一个元素，需要在元素后添加逗号
# 添加前
tup1 = (20)
print(tup1, type(tup1))

# 添加后
tup1 = (20,)
print(tup1, type(tup1))

print(tup1 * 2)
print(tup1 + name)

# 常用的操作
print('统计结果：', name.count('小红'))
print('获取下标：', name.index('小红'))  # 有多个相同的元素，默认获取打印第一个

