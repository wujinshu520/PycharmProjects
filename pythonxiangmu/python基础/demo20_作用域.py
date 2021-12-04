# 作用域：全局作用域，局部作用域
'''
1、作用域相对的

'''

name = '张三'  # 全局作用域


def test():
    #   name = '李四'  # 局部作用域，局部优先
    global name # 强制使用全局作用域
    name = '王五'
    print('我的名字是：', name)


print(name)
test()
