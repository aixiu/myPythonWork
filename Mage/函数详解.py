#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一个函数login，参数名称为host, port, username, password
# def login(host='127.0.0.1', port='8080', username='aixiu', password='shendlax'):
#     print('{}:{}@{}/{}'.format(host, port, username, password))

# login()
# login('127.0.0.1', 80, 'tom', 'tom')
# login('localhost', port=80, password='com')
# 主要练习函授参数的顺序，简单的往前，复杂的往后，位置参数靠前，默认参数在后

# 例二 有多个数，需要累加求和
# def add(nums):
#     sum = 0
#     for x in nums:
#         sum  += x
#     return sum

# add([1, 3, 5])
# add((2, 4, 6))
# 此例，nums 是一个形参，只能传入一个参数或是一个可迭代对象

# 例三 可变位置参数 *nums
# def add(*nums):
#     sum = 0
#     print(type(nums))
#     for x in nums:
#         sum  += x
#     print(sum)

# add(3, 6, 9)  # 调用

# 在形参前使用 * 表示该形参是可变位置参数，可以接收多个实参，收集多个实参为一个元组


# 例四 可变关键字参数 **kwargs
def showconfig(**kwargs):
    for k, v in kwargs.items():
        print('{} = {}'.format(k, v))

showconfig(host='127.0.0.1', port='8080', username='aixiu', password='shendl')
# 形参前使用 ** 符号，表示可以接收多个关键字参数，收集的实参名称和值组成一个字典
