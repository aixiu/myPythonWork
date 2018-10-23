#!/usr/bin/env python
# -*- coding: utf-8 -*-

def logger(fn):   # 相当于传入了add函数
    def inner(*args, **kwargs): # 新建一个包装函数，inner 
        ret = fn(*args, **kwargs)   # 把上边传入的函数进行调用。
        return ret
    return inner  # 返回包装函数，形成闭包，返回的函数是对原有函数进行的包装

@logger  # add = logger(add)
def add(x, y):
    return x + y

# foo = logger(add)
# print(foo(4, 6))



print(add(4, 6))