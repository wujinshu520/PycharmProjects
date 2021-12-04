# break: 跳出整个循环（结束整个循环）
# continue ： 跳出档次循环，会执行下一轮循环

name = ['李一', '李二', '李三', '李四']
for i in range(len(name)):
    print(name[i])
    # break
    continue
    print('测试')
else:
    # print('当条件不成立的时候会执行')
    pass  # 空语句，起占位作用
