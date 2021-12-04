# 作用域是相对，都是只在局部生效，局部优先
a = 10  # 全局作用域
def pri():
    a = 20  # 嵌套作用域
    def pri2():  # 函数中嵌套函数，相当于是局部函数，只能在pri函数里面才能调用
        a = 30  # 局部作用域
        print(a)
    pri2()
    print(a)

print(a)
pri()
