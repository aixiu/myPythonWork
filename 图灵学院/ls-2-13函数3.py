#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一个函数，打印一行九九乘法表
    # version 3.0
def jiujiu():
    for row in range(1, 10):
        for col in range(1, row+1):
            # print函数默认任务打印完毕后换行
            print( row * col, end=' ')
        print()
    return None
  
# 九九乘法表

jiujiu()

# 改造上面的函数

def printLine(linu_num):
    '''
    只负责打印一行九九乘法表
    linu_num 表示行号
    '''
    for i in range(1, linu_num + 1):
        print(linu_num * i, end=' ')
    print()

def jiujiu():
    for row in range(1, 10):        
        printLine(row)
    return None

jiujiu()


# 参数详解
    #参数分类
        # 普通参数/位置参数
        # 默认参数
        # 关键字参数
        # 收集参数

# 普通参数案例

def normal_para(one, two):
    print(one + two)
    return None
normal_para(1, 2)

# 默认参案例

def default_para(one, two, three=100):
    print(one + two)
    return None
default_para(2, 3)


# 关键字参数案例
def keys_para(one, two, three=30):
    print(one + two)
    return None
default_para(two=2, three=30, one=1)