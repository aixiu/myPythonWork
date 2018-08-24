#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机函数创建一个列表，进行大小排序，此方法称为冒泡法。

import random

numlist = []     # 定义一个列表

for i in range(10):          # 产生一个随机数，并把每次产生的数添加到numlist列表中，共10个
    numlist.append(random.randrange(1,10))

# print('生成的随机列表为>>> ', numlist)   # 打印当前生成的随机列表
print('{:=^23}\n'.format("生成的随机列表为"), numlist)   # 打印当前生成的随机列表

i = len(numlist) - 1   # 总排序次数

while i > 0:
    j = 0   # numlist 列表的初始下标
    while j < i:
        if numlist[j] > numlist[j+1]:
            numlist[j],numlist[j+1] =  numlist[j+1],numlist[j]

        j += 1

    # for k in numlist:
    print('\n{}'.format('当前排序后为>>>'), numlist, end='')
    i -= 1
# print('\n{}'.format('排序后为>>>'), numlist, end='')



# 方法二：

# def bubbleSort(nums):
#     for i in range(len(nums)-1):    # 这个循环负责设置冒泡排序进行的次数
        for j in range(len(nums)-i-1):  # ｊ为列表下标,负责每个小步骤的进行，并提供索引
#             if nums[j] > nums[j+1]:
#                 nums[j], nums[j+1] = nums[j+1], nums[j]
#     return nums

# nums = [5,2,45,6,8,2,1]

# print(bubbleSort(nums))



# 方法三：

# list1 = [5,2,45,6,8,2,1]
# for i in range(len(list1)-1):    # 这个循环负责设置冒泡排序进行(大步骤)的次数
#     for index in range(len(list1)-i-1):  # 负责每个小步骤的进行，并提供索引
#         if list1[index] > list1[index+1]:
#             list1[index], list1[index+1] = list1[index+1], list1[index]
#     print(list1)