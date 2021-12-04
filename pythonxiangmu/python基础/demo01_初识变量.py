"""
1、pythonxiangmu 中的变量不需要声明
2、pythonxiangmu 中的变量是没有类型的，类型是属于变量的值
"""

a = 5  # 单个变量复制
c = d = e = 1  # 多个变量赋相同的值，内存地址相同
x, y, z = 1, 2, 3  # 多个变量赋不同的值
print(a)
print(c, d, e)
print(x, y, z)
print("c的内存地址是", id(c))
print("d的内存地址是", id(d))
print("e的内存地址是", id(e))

# pythonxiangmu 标识符规则：
# 1、由字母、数字、下划线组成
# 2、不能以数字开头
# 3、不能以关键字作为标示符
import keyword  # 导入包

print("查看系统关键字：", keyword.kwlist)

# 4、标识符区分大小写
w = 5
W = 10
print(w)
print(W)

# 标识符命名编写规则
UserName = "张三"  # 大驼峰
userName = "李四"  # 小驼峰
user_name = "王五"  # 下划线

