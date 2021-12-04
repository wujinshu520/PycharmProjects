import time

# 时间，日期
# 1、用时间元组
# (年，月，日，时，分，秒，一周的第几日，一年的第几日，夏令时)
t=(2021,8,23,20,36,50,0,0,0)

# 2、时间戳
# 获取当前的时间戳
print(time.time())

# 给定时间的时间戳
print(time.mktime(t))

# 将时间戳转换成普通时间
print(time.localtime(1629722210.0))


# 3、格式化显示
print(time.strftime('%Y-%m-%d %H:%M:%p',t))
print(time.strptime('2021-08-23 20:36:50','%Y-%m-%d %X'))

# 4、英文显示
print(time.asctime(t))