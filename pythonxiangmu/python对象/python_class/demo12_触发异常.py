'''

异常的分类：
1、系统异常：
    下标越界，路径错误，值错误
2、业务异常：
    年龄范围只能1-120之间
    充值只能是正整数
    账号密码错误


# 触发异常由raise 关键字进行触发，只要raise就会报错
try:
    print('好好学习，天天向上')
    raise IndexError('我是下标越界错误！！！') #  创建了一个报错对象，并且给它赋值
except IndexError as e:
    print(e)

'''


# 输入的值只能是0-100之间的数字
# 自定义业务异常类
class OnlyInput0100Error(Exception):
    def __str__(self):
        return '输入的值的不再0-100范围之内。'


try:
    num = int(input('请输入1-100之间的数字:'))
    if num < 0 or num > 100:
        # 手动触发异常
        raise OnlyInput0100Error()
    else:
        print('您输入的数字是：', num)
except OnlyInput0100Error as e:
    print(e)
    print('系统默认num为null')
except Exception as e:
    print(e)
