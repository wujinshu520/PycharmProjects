# 异常处理: 处理软件或信息系统中出现的异常状况
# 语法：try  ---  except ----else ---finanlly

try:  # try 下面监控可能出现错误的代码
    num = int(input('请输入0-4之间的数字：'))
    lista = [1, 2, 3, 4, 5]
    print(lista[num])  # 下标越界错误

# 出错之后从上往下依次匹配看是否能匹配到对应的错误处理
except IndexError as e:  # 对下标越界错误进行处理
    print('下标越界,系统默认打印第一个值:', lista[0])
    print(e)
except ValueError as e:
    print('输入的类型错误：', e)
except Exception as e:
    print('未知错误，错误信息是：{}'.format(e))
else:   # 当try中没有错误的时候则执行else中的代码，有错误的时候则不执行
    print('hello world!!!')
finally:
    print('不管是否报错，我都会执行！！！！')
print('我是最后面的测试语句！！！！！！')