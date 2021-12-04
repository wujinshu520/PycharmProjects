# for 循环，就是遍历
'''

for 迭代变量 in 可迭代对象：
    执行语句....
eles:
    执行语句....

'''

lista = ['貂蝉', '吕布', '李小龙']
str = 'hello world'
for s in str:
    print(s)
print('------------------')

# range() 函数，作用是生成数列
# 生成0-4，最后一个数字是取不到的
for i in range(5):
    print('输出结果是：', i)

# 生成5-10，表示从第一个参数开始取到10
for i in range(5, 11):
    print('输出结果是：', i)

# 生成1，3，5，.... 表示从第一个参数开始，每次增加2，直到10结束
for i in range(1, 10, 2):
    print('输出结果是：', i)

# for 循环实现从1+2+3+....+100的和
print('for循环1到100相加的结果是：',sum(range(1,101)))