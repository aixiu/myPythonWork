#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 汉诺塔的问题
# 规则：
    # 1、每次移动一个盘子
    # 2、任何时候大盘子在下面，小盘子在上面
# 方法：
    # 1、n=1： 直接把A上的一个盘子移动到C上， A->C
    # 2、n=2:
        # A:把小盘子从A放到B上， A->B
        # B:把大盘子从A放到C上， A->C
        # C:把小盘子从B放到C上， B->C
    # 3、n=3:
        # A:把A上的两个盘子，通过C移动到B上去， 调用递归实现
        # B:把A上剩下的一个最大盘子移动到C上， A->C
        # C:把B上两个盘子，借助于A，挪到C上去， 调用递归
    # 4、n = n：
        # A:把A上的n-1个盘子，借助于C，移动到B上去，调用递归
        # B:把A上的最大盘子，也是唯一一个，移动到C上，A->C
        # C：把B上n-1个盘子，借助于A，移动到C上， 调用递归

# 代码如下
def hano(n, a, b, c):
    '''
    汉诺塔的递归实现
    n：代表几个盘子
    a：代表第一个塔，开始的塔
    b：代表第二个塔，中间过渡的塔
    c：代表第三个塔, 目标塔
    '''
    if n == 1:
        print(a, '-->', c)
        return None

    if n == 2:
        print(a, '-->', b)
        print(a, '-->', c)
        print(b, '-->', c)
        return None

    # 把n-1个盘子，从a塔借助于c塔，挪到b塔上去
    hano(n-1, a, c, b)
    print(a, "-->", c)
    # 把n-1个盘子，从b塔，借助于a塔，挪到c塔上去
    hano(n-1, b, a, c)

a = "A"
b = "B"
c = "C"

n = 10
hano(n, a, b, c)


# 第二种  利用递归函数移动汉诺塔:
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')