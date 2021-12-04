# String 字符串

str1 = '人生可以归结为一种简单的选择：不是忙着活，就是忙着死'
str2 = "坚强的人只能救赎自己，伟大的人才能拯救他人"
str3 = """这就是音乐的美丽。他们无法把这种美丽从你哪里夺去"""

print(str1)
print(str2)
print(str3)

# 推荐使用单引号
'''多行注释'''
"""多行注释"""

# 字符串切片（截取字符串的内容），下标从0开始（从左往右）从右往左那么下标是从-1开始
str4 = 'hello world!!!'
print("截取0-5的内容：", str4[0:5])  # 切片的时候不包含最后的下标
print("截取指定的某个下标:", str4[6])
print("从某个位置截取到最后", str4[6:])
print("从右往左截，截第一个：", str4[-1])
print("从右往左，截取的内容：", str4[-8:-3])

# 字符串操作：* +
str5 = '好好学习'
str6 = '天天向上'
print("复制内容:", str5 * 3)
print("连接两个字符串:", str6 + str5)

# 字符串常用方法
str7 = 'hello World'
# 1、将首字母变成大写
print(str7.capitalize())

# 2、都变成小写
print(str7.lower())

# 3、都变成大写
print(str7.upper())

# 4、替换指定的字符
print(str7.replace('o', 'X'))  # 替换所有的o
print(str7.replace('W', 'o', 1))  # 数字表示要替换的个数

# 5、用指定的符号进行分割
str8 = '猫#狗#老虎#狮子#凤凰'
list1 = str8.split('#')
print(list1)

# 格式化输出
name = '张三'
age = 21
print('我的名字叫：', name, '我今年', age, '岁')
print('我的名字叫：' + name + '我今年', age, '岁')
print('我的名字叫%s，我今年%d岁' % (name, age))

num = 100
# 十进制输出
print(num)
print('num=%d' % (num))
print('num=%i' % (num))

# 八进制
print('num=%o'%(num))

# 十六进制,不带符号
print('num=%x'%(num))
print('num=%X'%(num))

# 科学
print('num=%e'%(num))
print('num=%E'%(num))

# 浮点数
print('num=%f'%(num))
