# 函数
'''
 def 函数名称(参数列表)：
    语句块
'''


# a,b 是行参
def add(a, b):  # 有参函数
    return a + b


def pri():  # 无参函数
    print('我是无参函数1')
    return
    print('我是无参函数2')


# 调用：函数名()
print(add(2, 3))  # 2,3 是实参
pri()
