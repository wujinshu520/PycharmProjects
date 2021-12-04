# 读取文件内容

file_txt = open('/Users/zhang/Desktop/资料/python.txt', 'r',encoding='UTF-8')

# 1、 read 无参数的时候，默认全部读完，结果是当中一个字符串
# thing = file_txt.read()
# print(thing, type(thing))
# file_txt.close()
# print('----------------------------')

# 2、read 有参数时,该参数表示读取的字符数
thin = file_txt.read(5)
thin2 = file_txt.read(6) # 会从上一次的地方开始读取
print(thin, type(thin))
print(thin2, type(thin2))
file_txt.close()

# 3、按行读取
# readline方法没有参数默认读取一行
# readline方法有参数默认读取的字符数
# thin3 = file_txt.readline(25)
# print(thin3)
# file_txt.close()

# readlines 的参数超过一行的数量就会自动打印下一行的所有内容
# thin3 = file_txt.readlines(20)
# print(thin3)
# file_txt.close()

