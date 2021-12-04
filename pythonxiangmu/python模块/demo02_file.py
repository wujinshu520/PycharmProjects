# 文件操作：io流
# 文件对象名称 = open('文件路径'、'权限'、'缓冲')

# 创建一个文件对象
file_txt = open('/Users/zhang/Desktop/资料/python.txt','w')
print('编码是：',file_txt.encoding)
print('文件名称是：',file_txt.name)
print('权限是：',file_txt.mode)
print('是否关闭：',file_txt.closed)
file_txt.close() # 关闭流
print('是否关闭：',file_txt.closed)



