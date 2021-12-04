# if 判断语句
'''

if 表达式：
    语句块1   # 当表达式为True的时候执行
else：
    语句块2   # 当表达式False的时候执行

'''

# 从键盘上输入2个数字，然后输出大的那个数字

a = int(input('请输入第一个数字：'))
b = int(input('请输入第二个数字：'))
if a > b:
    print('输出结果为：', a)
else:
    print('输出结果为：', b)


# 红绿灯：红灯停，绿灯行，黄灯要停止走
# 1、红灯打印输出  红灯停
# 2、绿灯打印输出  绿灯行
# 3、黄灯打印输出  黄灯要停止走
color = input('请输入灯的颜色：')
if color == '红':
    print('红灯停')
elif color == '绿':
    print('绿灯行')
elif color == '黄':
    print('黄灯停止走')
else:
    print('输入结果错误')



