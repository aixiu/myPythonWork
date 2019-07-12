#!/usr/bin/env python
# -*- coding: utf-8 -*-

# filter 函数
    #  过滤函数：对一组数据进行过滤，符合条件的数据会生成一个新的列表并返回。
    # 跟map相比较：
        # 相同：都对列表的每个无素逐一进行操作。
        # 不同：
            # map会生成一个跟原来数据相对应的新队列
            # filter不一定，只要符合条件的才会进入新的数据集合
        # filter 函数怎么写：
            # 利用给定函数进行判断
            # 返回值一定是个布尔值
            # 调用格式：filter(f, data)  f 是过滤函数，data 是数据

# filter 案例

# 对于一个列表，对其进行过滤，偶数组成一个新列表

# 需要定义过滤函数
    #　过滤函数要求有输入，返回布尔值

def isEven(a):
    return a % 2 == 0

l = [3, 4, 55, 56, 433, 67, 4, 88]

rst = filter(isEven, l)
# 返回的filter 同容是一个可迭代对象
print(rst)

print([i for i in  rst])

print('--------------------')

# 高阶函数-排序
    # 把一个序列按照给定算法进行排序
    # key: 在排序前对每个元素进行key函数运算， 可以理解成按照 key 函数定义的逻辑进行排序
    # python2 和 python3 相差巨大

# 排序案例 1

a = [4, 55, 32, 89, 44, 53, 99, 123,222]

print(sorted(a))
print(sorted(a, reverse=True))

print('--------------------')

# 排序案例 2
a = [-43, 23, 45, 6, -23, 2, -234]
# 按照绝对值排序
# abs 是求绝对值的意思
# 即按照绝对值的倒序排列

al = sorted(a, key=abs, reverse=True)
print(al)

# sorted 案例

astr = ['dana', 'Dana', 'wangxiangjing', 'jingjing']

str1 = sorted(astr)
print(str1)

str2 = sorted(astr, key=str.lower)
print(str2)

print('--------------------')
# 返回函数
    # 函数可以返回具体的值
    # 也可以返回一个函数作为结果

# 定义一个普通函数
def myF(a):
    print('In myF')
    return None

a = myF(8)
print(a)

# 函数作为返回值反回，被返回的函数在函数体内定义

def myF2():
    def myF3():
        print('In myF3')
        return 3
    return myF3

# 使用上面定义
    # 调用 myF2 ,返回一个函数 myF3,赋值给f3

f3 = myF2()
print(type(f3))
print(f3)

f3()

print('--------------------')

# 负责一点的返回函数例子
    # args:参数列表
    # 1.myF4定义函数，返回内部定义的函数 myF5
    # 2.myF5使用了外部变量，这个变量是 myF4 的参数

def myF4(*args):
    def myF5():
        rst = 0
        for n in args:
            rst += n
        return rst

    return myF5

# 调用
f5 = myF4(1, 2, 3, 4, 5, 6, 7, 8, 9, 0)

# f5 的调用方式
f5()

print('--------------------')

# 闭包
    # 当一个函数在内部定义函数，并且内部的函数应用外部函数的参数或者局部变量，
    # 当内部函数被当做返回值的时候，相关参数和变量保存在返回的函数中，这种结果，叫闭包
    # 上面定义的myF4是一个标准闭包结构

# 闭包常见坑
def count():
    # 定义列表，列表里存放的是定义的函数
    fs = []
    for i in range(1,4):
        # 定义了一个函数f
        # f是一个闭包结构
        def f():
            return i*i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())

# 出现的问题：
    # 造成上述状况的原因是,返回函数引用了变量i，
    #  i并非立即执行，而是等到三个函数都返回的时候才统一使用，
    # 此时i已经变成了3，最终调用的时候，都返回的是 3*3

    # 此问题描述成：返回闭包时，返回函数不能引用任何循环变量

    # 解决方案： 再创建一个函数，用该函数的参数绑定循环变量的当前值，
    # 无论该循环变量以后如何改变，已经绑定的函数参数值不再改变

# 修改上述函数
def count2():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1,4):
        fs.append(f(i))
    return fs

f1,f2,f3 = count2()
print(f1())
print(f2())
print(f3())

print('--------------------')


# 装饰器
def hello():
    print('Hellp world')

hello()

f = hello
f()

# f 和 hello 是一个函数

print(id(f))
print(id(hello))
print('--------------------')
print(f.__name__)
print(hello.__name__)

    # 现在由新的需求：
    # 对hello功能进行扩展，每次打印hello之前打印当前系统时间
    # 而实现这个功能又不能改动现有代码
    # ==>使用装饰器

# 装饰器（Decrator）
    # 在不改动函数代码的基础上无限制扩展函数功能的一种机制，本质上讲，装饰器是一个返回函数的高阶函数
    # 装饰器的使用： 使用@语法， 即在每次要扩展到函数定义前使用@+函数名

# 任务：
    # 对hello函数进行功能扩展，每次执行hello万打印当前时间

import time

# 高阶函数，以函数作为参数

def printTime(f):
    def wrapper(*args, **kwargs):
        print('Time: ', time.ctime())
        return f(*args, **kwargs)
    return wrapper

# 上边定义了装饰器，使用的时候需要用到@ 此符号是python的语法糖

@printTime
def hello():
    print('Hello world')

hello()

# 装饰器的好处是，一点定义，则可以装饰任意函数
# 一旦被其装饰，则把装饰器的功能直接添加到定义函数的功能上
print('--------------------')

@printTime
def hello2():
    print("今天很高兴，被老板揪着讲课了")
    print("还可以由很多的选择")

hello2()


# 上面对函数的装饰使用了系统定义的语法糖
# 下面开始手动执行下装饰器
# 先定义函数

def hello3():
    print("我是手动执行的")
    
hello3()

hello3 = printTime(hello3)
hello3()

f = printTime(hello3)
f()

print('--------------------')

# 偏函数

# 把字符串转化成十进制数字
int("12345")

# 求八进制的字符串12345，表示成十进制的数字是多少
int("12345", base=8)

# 参数固定的函数，相当于一个由特定参数的函数体
# functools.partial的作用是，把一个函数某些函数固定，返回一个新函数

import functools
#实现上面int16的功能
int16 = functools.partial(int, base=16)

int16("12345")