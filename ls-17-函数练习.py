#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 给定一个数，利用函数求不同形状的面积

# 给的一个圆就算圆的面积，给的一个距形就算距形的

import math   # 导入数学运算模块

# 对输入的图形分流，如果是rectangle则用rectangl_area()，反之用circle_area()
def get_area(shape):
    shape = shape.lower()  # 字符串字母变为小写

    if shape == 'rectangle':
        rectangl_area()
    elif shape == 'circle':
        circle_area()
    else:
        print('请输入rectangle or cirle >>> ')

# 对分流后距形的运算
def rectangl_area():
    length = float(input('请输入长度>>> '))
    width = float(input('请输入宽度>>> '))

    area = length * width  # 面积算法

    print('长方形的面积为>>> ',area)

# 对分流后圆的运算
def circle_area():
    radius = float(input('请输入圆的半径>>> '))
    area = math.pi * math.pow(radius, 2)   # 圆的面积，用到math函数，pi=3.141592  pow幂运算参数radius的2次方 

    print('圆的面积为>>> {:.2f}'.format(area))  # 对符串格式化，取小数点后两位

# 主程序
shape_type = input('你想输入什么图形? rectangle or circle >>> ')

get_area(shape_type)  # 调用函数对数据处理