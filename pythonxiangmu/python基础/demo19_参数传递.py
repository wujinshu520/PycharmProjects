# 参数传递

# 1、参数是不可变数据类型： 传递的是实参的zhi
def add(a, b):
    return a + b


print('参数传递后计算结果：', add(3, 6))


# 2、参数是可变数据类型：传递的是实参的地址, 引用传递
def test_list(mylist):
    print(id(mylist))
    mylist.append([1, 2, 3])
    print('列表是：', mylist)


list1 = ['a', 'b']
test_list(list1)
print(list1)
print(id(list1))
