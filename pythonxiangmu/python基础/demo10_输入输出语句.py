# 输入，输出语句
'''
# 注意：默认输入的所有内容都是str类型
# str = input('请输入内容：')
# print(type(str),str)
'''

'''
# 练习：从键盘上输入自己的姓名，年龄，家乡，打印输出
name = input('姓名：')
age = int(input('年龄：'))
home = input('家乡：')
print('我叫%s,我今年%d岁，我的家乡是%s' % (name, age, home))
'''

# .format格式化输出：字符串.format(参数)
print('我的名字叫:{},我喜欢{}'.format('吕布', '貂蝉'))
print('我的名字叫:{1},我喜欢{0}'.format('吕布', '貂蝉'))
print('我的名字叫:{name},我喜欢{likename}'.format(name='吕布', likename='貂蝉'))

# 练习：从键盘上输入自己的姓名，年龄，家乡，打印输出
print('我的名字叫:{},我的年龄：{},我的家乡是：{}'.format('吴进书', '25', '贵州独山'))
