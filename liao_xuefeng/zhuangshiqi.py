#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 装饰器的学习资料

# 关于作用域，我们要理解两点：
# a、在全局不能访问到局部定义的变量
# b、在局部能够访问到全局定义的变量，但是不能修改全局定义的变量（当然有方法可以修改）

# 实例一

# def w1(func):
#     print('...装饰器开始装饰...')

#     def inner():
#         print('...验证权限...')
#         func()

#     return inner

# @w1   #相当于下边的 test = w1(test)  
# def test():
#     print('test aaa')

# # test = w1(test)

# test()  # 此时的test()不是原来的test(),而是w1.inner()的返回结果

# # 实例二

# def makeBold(fun):
#     print('----a----')

#     def inner():
#         print('----1----')
#         return '<b>' + fun() + '</b>'

#     return inner


# def makeItalic(fun):
#     print('----b----')

#     def inner():
#         print('----2----')
#         return '<i>' + fun() + '</i>'

#     return inner


# @makeBold
# @makeItalic
# def test():
#     print('----c----')
#     print('----3----')
#     return 'hello python decorator'


# ret = test()
# print(ret)

# # test()

# 实例三

a_string = "This is a global variable"
def foo():
    a_string = 'test'
    print(a_string) # 1
foo()

print(a_string)
