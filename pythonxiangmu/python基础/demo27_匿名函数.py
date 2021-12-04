# 匿名函数
'''
语法：
    lambda 参数列表：返回的表达式
'''


# 使用lambda实现加法运算
def add(a, b):
    return a + b

sum = lambda a, b: a + b
print(sum(8,9))
