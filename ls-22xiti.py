#!/usr/bin/env python
# -*- coding: utf-8 -*-

# '''
# ****
# *  *
# *  *
# ****

# 0000000000000000000
# 0                 0
# 0                 0
# 0000000000000000000
# '''

def boxPrint(symbol, width, heigth):  # 定义一个函数并设置三个参数为：输入的字符，宽度和高度
    if len(symbol) != 1:     # 如果字符字符数不为1，侧提示只能输入一个字符        
        raise Exception('Symbol must be a single character')  
    if width <= 2:     # 如果宽度小于等于2，则提示最少输入2
        raise Exception('Width must be greater than 2')
    if heigth <= 2:    # 如果高度小于等于2，则提示最少输入2
        raise Exception('heigth must be greater than 2')

    print(symbol * width)    # 打印第一行

    for i in range(heigth - 2):   # 打印中间两行
        print(symbol + ' ' * (width - 2) + symbol)

    print(symbol * width)   # 打印最后一行
    print()    # 每个图形打印完，再打一个回车
    

for sys, w, h in (('*', 4, 4),('0', 20, 2),('X', 2, 3),('#', 3, 3)):
    try:
        boxPrint(sys, w, h)
    except Exception as err:   # 把系统出错内容写入err 然后打印出系统出错内容
        print('An exception happened: ' + str(err)+ '\n')