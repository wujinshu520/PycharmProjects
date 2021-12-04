# 修改文件的读写位置，位移

file_txt = open('/Users/zhang/Desktop/资料/py.txt', 'rb')
print(file_txt.read(3))
print(file_txt.tell())  # 获取当前的位置
# 0 表示从文件的开头位置，1表示当前位置，2表示文件末尾
# 在文件中没有使用b模式（二进制）打开文件，那么只允许从文件开头计算相对位置
file_txt.seek(4,1)
print(file_txt.read(3))
file_txt.close()
