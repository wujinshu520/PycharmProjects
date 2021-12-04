# 数据类型：number（int,float,bool,complex）
import sys

a = 5  # int 整数
b = 3.14  # float 浮点型
# 查看数据类型
print("类型是：", type(a))
print("类型是：", type(b))

# bool   T或F必须要大写   Ture --- 1    False --- 0
c = True  # bool 布尔类型
# print("类型是：", type(c))

e = 3 + 5j  # complex 复数 a+bj
print("类型是：", type(e))

# 查看所占的内存空间大小
print("内存空间大小：", sys.getsizeof(a))
print("内存空间大小：", sys.getsizeof(b))
