# 写入内容

file_txt = open('/Users/zhang/Desktop/资料/py.txt', 'a+',encoding='UTF-8')
file_txt.write('are you ok')
file_txt.flush()  # 将内容从缓存提交到硬盘，只要文件内容发生改动就必须要flush
file_txt.close()