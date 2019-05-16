#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 异常
    # 广义上的错误分为错误和异常
    # 错误指的是可以人为避免
    # 异常是指在语法逻辑正确的前提下，出现的问题
    # python 里，异常是一个类，可以处理和使用

# 异常的分类
    # AssertError 断言语句（assert）失败
    # AttributeError 尝试访问未知的对象属性
    # EOFError 用户输入文件末尾标志EOF（Ctrl+d）
    # FloatingPointError 浮点计算错误
    # GeneratorExit generator.close()方法被调用的时候
    # ImportError 导入模块失败的时候
    # IndexError 索引超出序列的范围
    # KeyError 字典中查找一个不存在的关键字
    # KeyboardInterrupt 用户输入中断键（Ctrl+c）
    # MemoryError 内存溢出（可通过删除对象释放内存）
    # NameError 尝试访问一个不存在的变量
    # NotImplementedError 尚未实现的方法
    # OSError 操作系统产生的异常（例如打开一个不存在的文件）
    # OverflowError 数值运算超出最大限制
    # ReferenceError 弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
    # RuntimeError 一般的运行时错误
    # StopIteration 迭代器没有更多的值
    # SyntaxError Python的语法错误
    # IndentationError 缩进错误
    # TabError Tab和空格混合使用
    # SystemError Python编译器系统错误
    # SystemExit Python编译器进程被关闭
    # TypeError 不同类型间的无效操作
    # UnboundLocalError 访问一个未初始化的本地变量（NameError的子类）
    # UnicodeError Unicode相关的错误（ValueError的子类）
    # UnicodeEncodeError Unicode编码时的错误（UnicodeError的子类）
    # UnicodeDecodeError Unicode解码时的错误（UnicodeError的子类）
    # UnicodeTranslateError Unicode转换时的错误（UnicodeError的子类）
    # ValueError 传入无效的参数
    # ZeroDivisionError 除数为零

l = [1, 2, 3, 4, 5]
# 常范的除零错误
num = int(input('plz input you num:'))
print(100/num)

# 异常处理
    # 不能保证程序永远正确运行
    # 但是，必须保证程序在最坏的情况下得到的问题被妥善得处理
    # python 的异常处理模块全部语法为：
        # try:
        #     尝试实现某个操作，
        #     如果没出现异常，任务就可以完成
        #     如果出现异常，将异常从当前代码块扔出去尝试解决异常

        # except 异常类型1:
        #     解决方案1：用于尝试在此处处理异常解决问题

        # except 异常类型2：
        #     解决方案2：用于尝试在此处处理异常解决问题

        # except (异常类型1,异常类型2...):
        #     解决方案：针对多个异常使用相同的处理方式

        # excpet:
        #     解决方案：所有异常的解决方案

        # else:
        #     如果没有出现任何异常，将会执行此处代码

        #   finally:
        #       管你有没有异常都要执行的代码

# 流程
    # 执行try下面的语句
    # 如果出现异常，则在except语句里查找对应异常病进行处理
    # 如果没有出现异常，则执行else语句内容
    # 最后，不管是否出现异常，都要执行finally语句
    # 除except(最少一个)以外，else和finally可选

# 简单异常安全
try:
    num = int(input('Plz input you nuber:'))
    rst = 100/num
    print('计算结果是: {}'.format(rst))
except:
    print('你输的是什么玩意儿')
    # exit 是退出程序的意思
    exit()
