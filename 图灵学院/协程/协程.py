#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 协程

# - 参考资料
#   - http://python.jobbole.com/86481/
#   - http://python.jobbole.com/87310/
#   - https://segmentfault.com/a/1190000009781688

## 迭代器

# - 可迭代（Iterable）：直接作用于 for 循环的变量
# - 迭代器（Iterator）: 不但可以作用于 for 循环，还可以被next 调用
# - list 是典型的可迭代对象，但不是迭代器
# - 通过 isinstance 判断
# - iterable 和 iterator 可以转换
    # - 通过 iter 函数

# 可迭代
l = [i for i in range(10)]

# l 是可迭代对象，但不是迭代器
for idx in l:
    print(idx)

# ranger 是个 迭代器
for i in range(5):
    print(i)

#  isinstance 案例
    # 判断某个变量是否是一个实例

    # 判断是否可迭代

from collections.abc import Iterable


ll = [1, 2, 3, 4, 5]
print(isinstance(ll, Iterable))

from collections.abc import Iterator

print(isinstance(ll, Iterator))


# iter 函数

s = 'I lover ergouzi'

print(isinstance(s, Iterable))
print(isinstance(s, Iterator))

s_iter = iter(s)  # iter 函数转换

print(isinstance(s, Iterable))
print(isinstance(s, Iterator))


# 生成器
    # generator:一边循环一边计算工下一个元素的机制/算法
    # 需要满足三个条件：
        # 每次调用都生产出 for 循环需要的下一人元素或者
        # 如果达到最后一个后，提示，StopIteration 异常
        # 可以被 next 函数调用
    #如何生成一个生成器
        # 直接使用
        # 如果函数中包含 yield  ，则这个函数就叫生成器
        # next 调用函数，遇到 yield  返回

# 直接使用生成器
l = [x*x for x in range(5)]   # 放在中括号中是列表生成器

g = (x*x for x in range(5))  # 放在小括号中就是生成器

print(type(l))
print(type(g))


# 函数案例

def odd():
    print('Step 1')
    print('Step 2')
    print('Step 3')
    return None

odd()

# 生成器的案例

def odd():
    print('Step 1')
    yield 1
    print('Step 2')
    yield 2
    print('Step 3')
    yield 3

# odd() 是调用生成器
g = odd()

one = next(g)
print(one)

two = next(g)
print(two)

three = next(g)
print(three)


# for 循环调用生成器

def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1

    return 'Done'

fib(5)

# 斐波那契数列的生成器写法
def fib(max):
    n, a, b, = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a+b
        n += 1
    # 需要注意，抛出异常的返回值是 return 的返回值
    return 'Done'

g = fib(5)

# for i in range(6):
#     rst = next(g)
#     print(rst)

ge = fib(10)
'''
生成器的典型用法是在for 中使用
比较常用的典型生成器就是range
'''
for i in ge:
    print(i)



# 协程

    # 历史历程
        # 3.4引入协程， 用 yield 实现
        # 3.5引用协程语法
        # 实现的协程比较好的包有  asyncio, tornado, gevent

    # 定义：协程：是为非抢占式多任务产生子程序的计算程序组件，协程允许不同入口点在不同位
    # 置暂停或开始执行程序。
    # 从技术角度讲，协程就是一个你可以暂停执行的函数， 或者干脆把协程理解成为生成器。

    # 协程的实现：
        # yield 返回
        # send 调用

# 协程代码案例1

def simple_coroutine():
    print('--> start')
    x = yield
    print('--> recived', x)


# 主线程
sc = simple_coroutine()
print(1111)

# 可以使用 sc.send(None),效果一样
next(sc)   # 预激

print(2222)
sc.send('zhexiao')