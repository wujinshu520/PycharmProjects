# 函数嵌套

# 1、在函数内部调用其他函数
def pri():
    print('我是pri函数')


def pri2():
    pri()


pri2()
print('-------------------------')



# 2、在函数内部在定义一个函数（不常见）
def pri3():
    def pri4():  # 该方法只能够在当前函数中进行调用
        print('我是pri4函数')

    pri4()


pri3()
