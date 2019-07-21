#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数定义
def func():
    print('我爱王晓静')
    print('我想你了')

func()

# 函数的参数和返回值
    # 参数：负责给函数传递一些必要的数据或者信息
        # 形参（开式参数）：在函数定义时用到的能数，没有具体值，只是一个占位符号。
        # 实参（实际参数）：在调用函数的时候输入的值。
    # 返回值：调用函数的蚨卢的一个执行结果
        # 使用 return 返回结果
        # 如果没有值需要返回，我们推荐使用 return None 表示函数结束
        # 函数一但执行 return ，则函数立即结束
        # 如果函数没有 return关键字，则默认返回 None

# 形参和实参的案例。
    # 参数 person 只是一个符号
    # 调用时，用另一个。

def hello(person):
    print('{},你好吗？'.format(person))
    print('{},你看见我家二麻子了吗？'.format(person))

# 调用函数，需要把实际内容作为实参传入
hello('张三')
hello('李四')


pp = hello('大拿哥')
print(pp)

# help 负责随时为您提供帮助
help(print)


# 九九乘法表
    # version 1.0
for o in range(1, 10):  # 控制外循环，从1到9
    for i in range(1, o+1): # 内循环，每次从第一个数开始打始，打印到跟行数相同的数量
        print(o * i, end=' ') 
    print()


    # version 2.0
for i in range(1, 10):
    for j in range(1, i+1):        
        print('{} * {} = {}  '.format(j, i ,i*j), end='')
    print()