# list 列表
'''
特点：
1、可变数据类型
2、可以存放多种数据类型
3、数据可以重复
4、有下标，下标从0 开始

在python中有下标就能切片
'''

list1 = ['张三', '李四', '王五', 20, True, 3.14, 20, '李四']
print(list1, type(list1))
print('截取下标中1的内容：', list1[1])
print('截取下标中0-3的内容：', list1[0:3])
print('截取下标中2以后的内容：', list1[2:])
print('连接内容：', list1 * 2)

list2 = ['wuwuwu']
print('连接内容：', list1 + list2)

# 常用操作方法
list3 = [1, 2, 3, '小米']
print(list3)
print(id(list3))

# 追加元素
list3.append('小红')
print('内容展示：', list3)
print(id(list3))

a = 5
print(id(a))
a = 9
print(id(a))
b = 5
print(id(b))

# 在下标1的位置插入元素
list3.insert(1, '小米')
print(list3)

# 返回最后一个元素，并且将它从list中删除
list3.pop()
print(list3)

# 统计元素个数
print(list3.count('小米'))

# 删除第一次出现的该元素
list3.remove('小米')
print(list3)

# 将list4中的元素追加到list3中
list4 = ['a', 'b']
list3.extend(list4)
print(list3)

score = [40, 25, 80, 33, 90, 74, 50]
# 将分数从小到大排序
score.sort()  # 排序，默认是从升序排列
print('排序后的内容展示：', score)

# 将分数降序排列
score.reverse()  # 反转
print('反转后的内容展示：', score)

# 复制
listc = [1, 2, 3, 4, 5]
listd = listc  # 取别名，内存地址相同
print('列表内容有：', listc, '内存地址:', id(listc))
print('列表内容有：', listd, '内存地址:', id(listd))

liste = listc[:]  # 复制克隆，会开辟新的内存空间
print('列表内容有：', liste, '内存地址:', id(liste))

list_name = ['张一','张二','张三','张四','张五']
# 取指定的某个元素
print(list_name[2])
print(list_name)

# 遍历:访问某个集合中的所有元素，直到每个元素都被访问到就自动结束
for name in list_name:
    print(name)
