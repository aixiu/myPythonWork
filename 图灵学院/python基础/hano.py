#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 这是一个加了统计次数的功能
# 函数需要用到全局变量，定义在函数之外，函数中要使用前，需要在引用前加global。

tj = 0
def move(n, a, b, c):
    global tj

    if n == 1:
        print('move', a, '-->', c)
        tj += 1
        print('移动了{}次'.format(tj))
    else:
        # 把n-1个盘子，从a塔借助于c塔，挪到b塔上去
        move(n-1, a, c, b)
        # 此时，A塔上只有一个盘子，因为 n = 1 所以执行上边的 if 语句，直接将A挪到c塔上去
        move(1, a, b, c)
        # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上去      
        

move(3, 'A', 'B', 'C')