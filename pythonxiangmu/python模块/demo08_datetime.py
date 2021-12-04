import datetime

# 日期、时间
# 1、元组表示时间
t = datetime.datetime(2021, 8, 23, 21, 1, 45, 0)
print(t)

# 2、截取部分时间
print('年：', t.year)
print('月：', t.month)
print('日：', t.day)
print('日期：', t.date())
print('星期：', t.weekday())  # 0到6

# 3、获取当前系统时间
print(datetime.datetime.today())
print(datetime.datetime.now())

# 4、获取时间戳
print(t.timestamp())  # 将时间转换成时间戳

# 将时间转换成字符串
print('字符串是：', t.fromtimestamp(t.timestamp()))

# 5、自定义格式化输出
print(t.strftime('%Y-%m-%d %H:%M:%p'))

# 6、英文显示
print(t.ctime())
