# 选择排序
'''
1、每一次比较的时候都是交换下标
2、每一轮比较结束之后会互换一次位置


'''

score = [66, 46, 50, 35, 60, 20]
print('排序之前的结果：',score)
for i in range(len(score) - 1):  # 控制轮数
    min = i  # 默认最小下标
    for j in range(i + 1, len(score)):  # 控制比较次数，每一轮起始下标都是比前一轮起始下标多1
        if score[min] > score[j]:  # 交换下标
            min = j
    score[min], score[i] = score[i], score[min]  # 每一轮结束互换位置
    print('每%s轮的比较结果：' % (i + 1), score)
print('排序之后的结果：',score)
