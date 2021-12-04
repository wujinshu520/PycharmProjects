# 循环语句 while

'''

while 判断条件：
    执行语句.....
else:
    执行语句.....

'''

# 实现从1+2+3+....+100的和
sum = 0
i = 1
while i < 100:
    sum += i
    i = i + 1
else:
    print('条件不成立，没有执行循环')
print('相加到最后的结果：', sum)
print('--------------------------')

'''
# 练习：从键盘上输入一个分数，
# 1、分数的范围只能是0---100
# 2、假如分数不在这这个区间则提示： 输入错误，请重新输入
# 3、直到输入正确为止，然后打印出该分数
# 方式一：
secore = int(input('请输入0到100的分数：'))
while secore < 0 or secore > 100:
    secore = int(input('输入错误，请重新输入0到100的分数：'))
print('输出的分数结果：',secore)
print('--------------------------')
'''

# 方式二：
while (True):
    secore = int(input('请输入0到100的分数：'))
    if secore > 0 and secore <= 100:
        print('分数为：', secore)
        break  # 跳出整个循环
    else:
        print('请重新输入')
