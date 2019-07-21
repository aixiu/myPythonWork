# #!/usr/bin/env python
# # -*- coding: utf-8 -*-

# Log模块资料
# https://www.cnblogs.com/yyds/p/6901864.html

# Python语言的高级特性

# 函数式编程(FunctionalProgramming)
    # 基于lambda演算的一种编程方式
        # 程序中只有函数
        # 函数可以作为参数，同样可以作为返回值
        # 纯函数式编程语言： LISP， Haskell
    # Python函数式编程只是借鉴函数式编程的一些特点，可以理解成一半函数式一半Python

    # 需要讲述
        # 高阶函数
        # 返回函数
        # 匿名函数
        # 装饰器
        # 偏函数

# lambda表达式
# 函数： 最大程度复用代码

    # 存在问题： 如果函数很小，很短，则会造成啰嗦
    # 如果函数被调用次数少，则会造成浪费
    # 对于阅读者来说，造成阅读流程的被迫中断
    # lambda表达式（匿名函数）：

# 一个表达式，函数体相对简单
    # 不是一个代码块，仅仅是一个表达式
    # 可以有参数，有多个参数也可以，用逗号隔开

# ‘小’函数举例
def printA():
    print('AAAAA')

printA()


# lambda表达式的用法
    # 1、以lambda 开
    # 2、紧跟一定的参数（如果有的话）
    # 3、参数后用冒号和表达式主题隔开
    # 4、只是一个表达式，所以没有return

# 计算一个数字的100倍数
stm = lambda x: 100 * x
# 使用上跟函数调用一样
stm(25)


stm2 =  lambda x,y,z: x + y * 10 + z * 100
stm2(4, 5, 6)

# 高阶函数
    # 把函数作为参数使用的函数，叫高阶函数

# 变量可以赋值
a = 100
b = a

# 函数名称就是一个变量
def funA():
    print('In FunA')

funB = funA
funB()

# 以上代码得出的结论：
    # 函数名称是变量
    # funB 和 funA 只是名称不一样而已
    # 既然函数名称是变量，则应可以被当做参数传入另一个函数

# 高阶函数例子
    # funA 是普通函数，返回一个传入数字的100倍数字

def funA(n):
    return n * 100

    # 再写一个函数，把传入参数 乘以300倍

def funB(n):
    # 最终结果是想返回300n
    return funA(n) * 3

print(funB(9))

# 用高阶函数来写
def funC(n, f):
    return f(n) * 3

print(funC(9, funA))

# 比较funC 和 funB ，显然 funC 的写法要优于 funB
    # 例如：
def funD(n):
    return n * 10

# 需求变更，需要把 n放大三十陪，此时 funB则无法实现，因为代码写死

print(funC(9, funD))