def pri():
    print('我是a中的pri方法')


def pri2():
    print('hello')


# 判断当前自己是不是自己
if __name__ == '__main__':
    pri()
    pri2()

#__name__ 是指当前运行的主函数名称
print(__name__)
