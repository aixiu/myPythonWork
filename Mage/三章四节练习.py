#!/usr/bin/env python
# -*- coding: utf-8 -*-

#   打印一个边长为N的正方形
# reg = int(input('输入打印正方形的边长： '))   #正方形星数

# print('*' * reg)

# for i in range(reg - 2):
#     print('*'+' ' * (reg - 2)+'*')
# print('*' * reg)


# x = int(input('输入打印正方形的边长： '))   #正方形星数

# print(x * '*')
# for i in range(x -2):
#     print('*' + ' ' * (x - 2) + '*')

# print(x * '*')


#   打印100内所有奇数的和  2500
# res = [x for x in range(1, 100, 2)]
# print(sum(res))

# 判断成绩A~E 90以上A 80-89为B 70-79为C 60-69为D 60以下为E
chengji = int(input(('{}'.format('请输入成绩>>> '))))

if chengji >= 90:
    print('{}'.format('成绩为：A'))
elif chengji >= 80:
    print('{}'.format('成绩为：B'))
elif chengji >= 70:
    print('{}'.format('成绩为：C'))
elif chengji >= 60:
    print('{}'.format('成绩为：D'))
else:
    print('{}'.format('成绩为：E'))
