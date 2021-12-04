# LEGB法则：局部作用域>嵌套作用域>全局作用域>内置作用域

# print(__file__) # B 内置
# __file__= 10  # G 全局
def pri():
    # __file__ = 20  # E 嵌套
    def pri2():
        # __file__ = 30   # L 局部
        print(__file__)

    pri2()


pri()
