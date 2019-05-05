#!/usr/bin/env python
# -*- coding: utf-8 -*-

# for 循环练习
    # 简单的图形打印

'''
* * * * *
* * * * *
* * * * *
* * * * *
'''
# 例一
for i in range(0, 4):
    print('{}'.format("* " * 5))

# 改进上例，例二
for i in range(0, 4):
    for j in range(5):
        # print 默认自动换行，用 end 参数控制
        print('*', end=' ')
    print()

# for 循环练习
    # 简单的图形打印

'''
* * * * *
*       *
*       *
* * * * *
'''
# 例一
for i in range(4):
    if i == 0 or i == 3:
        print('* ' * 5)
    else:
        print('*       *')

# 改进上列代码
for i in range(4):
    if i == 0 or i == 3:
        print('* ' * 5)
    else:
        for j in range(5):
            if j == 0 or j== 4:
                print('*',end=' ')
            else:
                print(' ',end=' ')
        print()


