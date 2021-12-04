# 递归： 自己调用自己
'''
def pri():
    print('hello world !!!')
    pri()

pri()
'''

# 循环打印出N个hello world！！！
def pri(num):
    if num >0:
        print('hello world!!!')
        pri(num-1)
    else:
        return 0

pri(6)



