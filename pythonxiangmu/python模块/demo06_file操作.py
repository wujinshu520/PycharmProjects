# 文件操作
import os

# 1、重命名
#os.rename('/Users/zhang/Desktop/资料/py.txt','/Users/zhang/Desktop/资料/py_wu.txt')

# 2、删除文件
# os.remove('/Users/zhang/Desktop/资料/py_wu.txt')

# 3、目录操作
# os.mkdir('/Users/zhang/Desktop/资料/wujinshu')

# 4、删除目录
# os.rmdir('/Users/zhang/Desktop/资料/wujinshu')

# 5、创建多级目录
# os.makedirs('/Users/zhang/Desktop/资料/a/b/c')

# 6、获取当前工作目录
# print(os.getcwd())

# 7、改变当前目录
# os.chdir('/Users/zhang)

# 判断目录是否存在
print(os.path.isdir('/Users/zhang/Desktop/资料/a/b/c/test.txt'))
print(os.path.isfile('/Users/zhang/Desktop/资料/a/b/c/test.txt'))