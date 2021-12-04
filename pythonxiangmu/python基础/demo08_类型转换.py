# 数据类型转换
# 1、自动转换
# 2、强制转换

# 发生了自动转换，从低精度向高精度转换
a = 5
b = 3.14
print(a + b)
print(a + int(b))

# 进制转换   int(x,base)  base表示进制
print(int('123'))  # 字符串转换成十进制
print(int('123', 10))
print(int('123', 8))  # 8进制转换成10进制
print(int('7B', 16))  # 16 进制转换成10进制

# int 和 char 转换
a = 48
b = 57
c = 65
d = 90
print(chr(a), chr(b), chr(c), chr(d))

# char转int
A = 'A'
B = 'B'
print(ord(A), ord(B))
print(type(A))
