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