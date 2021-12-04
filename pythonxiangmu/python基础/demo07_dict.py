# 字典 dict
'''

特点：
1、可变数据类型
2、没有下标
3、元素都是键值对  {'name':'张三'}  key：value

注意：
1、字典中的健必须独一无二，但值则不必，创建时如果同一个健被赋值两次，后一个值会被记住
2、健必须不可变，可以用数字，字符串或元组

'''

info = {'name': '张三', 'age': '18', 'adderss': '上海'}
print(info, type(info))

# 新增元素
info['sex'] = '女'
info['age'] = 20
print(info)
print(info['name'])  # 通过key获取value

# 删除某个元素
del info['age']
print(info)

# 删除整个字典
# del info
# print(info)

# 字典常用方法
info2 = {'name': '张一', 'age': '18', 'adderss': '上海'}

# 获取所有的key
print(info2.keys())

# 获取所有的value
print(info2.values())

# 清空所有的元素
# info2.clear()
# print(info2)

# 获取key所对应的value，元素不存在则提示自定义信息
print(info2.get('name', '该键值对不存在'))

# 删除该键值对并且返回它的value
print(info2.pop('adderss') )
print(info2)

# 将dict1中的元素添加到info2中，有重复的key那么会跟新值
dict1 ={'email':'1964855301@qq.com','age':'21'}
info2.update(dict1)
print(info2)


# 遍历字典
# 1、遍历key
for i in info2.keys():
    print(i)
print('-------------------')


# 2、遍历value
for e in info2.values():
    print(e)
print('-------------------')

# 3、遍历所有的键值对
print(type(info2.items()))
for key,value in info2.items():
    print('key=%s  value=%s '%(key,value))

print('-------------------')

for key in info2.items():
    print('key=%s  value=%s '%key)







