# 序列： 字符串，列表，元组
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd']
str1 = 'hello world'

# 求长度
print(len(str1))

# 相连
print(list1 + list2)

# 相加
print(list1 * 3)

# 求是否序列中是否存在
print(4 in list1)

# 求最大值，最小值
print(max(list1), min(list1))

# 取部分数据求最大值，最小值
lista = [1, 2, 30, 4, 12, 21, 60]
print(max(lista[2:6]))  # 包前不包后
print(max(lista[2:][:6]))  # 包前又包后
print(max(lista[2:]))