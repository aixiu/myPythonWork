#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 什么是柯里化
# 指的是将原来接受两个参数的函数变成新接受一个参数的函数的过程。新的函数返回一个以原有第二个参数为参数的函数。
# 如：z = f(x, y)  转换成  z = f(x)(y)

# 实例
def add(x, y):
    return x + y
# z = f(x, y)

print(add(4, 5))

def new_add(x):
    return inner  
# 方便记忆的写法，先写一个函数，接受第一个参数，然后返回一个新的函数, 如，返回了一个新的函数 inner。

def new_add(x):
    def inner(y):
        return x + y
    return inner
# foo = new_add(4)
# foo(5)

print(new_add(4)(5))
# z = f(x)(y)

# 方便记忆写法，再内部再写一个函数，注意函数名为上一层函数返回的函数名，如：inner 在内部函数编写具体的函数实体。