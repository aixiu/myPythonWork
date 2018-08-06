#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 相关基础

# 第一，必须强调的是python是从上往下顺序执行的，
# 而且碰到函数的定义代码块是不会立即执行它的，只有等到该函数被调用时，
# 才会执行其内部的代码块。

# def foo():
#     print('这里是上面的函数定义~')
# def foo():
#     print('这里是下面的函数定义！')
# foo()

# 其次，我们还要先搞清楚几样东西：
# 函数名、函数体、返回值，函数的内存地址、函数名加括号、函数名被当作参数、
# 函数名加括号被当作参数、返回函数名、返回函数名加括号。对于如下的函数：

# def foo():
#     print('测试效果')
#     return 'ok'
# foo()


# def outer(some_func):
#     def inner():
#         print("before some_func")
#         ret = some_func() # 1
#         return ret + 1
#     return inner
# def foo():
#     return 1
# decorated = outer(foo) # 2
# # decorated()
# print(decorated())

# def a():
#     print(111)
#     return 'ok'

# def b():
#     print(222)
#     return a()
#     return 'aaa'

# print(b)
# print(b())

# def f():
#     print(1111)

# def a(b):
#     print(22222)
#     return f

# b =a(f)
# print(b())

# -------------------------------------------
# def outer(func):
#     def inner():
#         print('我是内层函数')
#     return inner()

# def foo():
#     print('我是原始函数')

# print(outer(foo))
# outer(foo())


# 实例装饰器

# def outer(func):
#     def inner(username):
#         print("认证成功！")
#         result = func(username)
#         print("日志添加成功")
#         return result
#     return inner

# # 基础平台部门开发了上百个函数
# @outer
# def f1(name):
#     print('{}正在连接数据接口'.format(name))


# #各分别调用
# f1('jack')


# def deco(func):     
#     print("1111")  
#     func()  
#     print("2222")
#     return func
 



def deco(func):  
    def _deco():  
        print("1111")  
        func()  
        print("2222")  
        # 不需要返回func，实际上应返回原函数的返回值  
    return _deco  
 
@deco  
def myfunc():  
    print("333")  
    return 'ok'  
  
myfunc()
