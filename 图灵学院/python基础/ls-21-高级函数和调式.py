#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 高级函数的补充

# zip
    # 把两个可迭代的内容生成一个可迭代的tuple 元组类型组成的内容

# zip 案例

l1 = [1, 2, 3, 4, 5]
l2 = [11, 22, 33, 44, 55]

z = zip(l1, l2)
print(type(z))

for i in z:
    print(i)

# enumerate
    # 跟 zip 功能比较像
    # 对可迭代对象里的每一个元素，配上一个索引，然后索引和内容构成 tuple 类型

l1 = [11, 22, 33, 44, 55]
em = enumerate(l1)

l2 = [i for i in em]
print(l2)

em = enumerate(l1, start=100)
l2 = [i for i in em]
print(l2)


# collections 模块
    # namedtuple
    # deque

    # namedtuple
        # tuplel 类型
        # 是一个可命名的 tuple

import collections

Point = collections.namedtuple('Point', ['x', 'y'])

p = Point(22, 44)

print(p.x)
print(p[1])


Circle = collections.namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(100, 150, 50)
print(c)
print(type(c))

# 想检测以下 namedtple 到底是属于谁的子类
print(isinstance(c, tuple))


# dequeue
    # 比较方便的解决了频繁删除插入带来的效率问题

from collections import deque

q = deque(['a', 'b', 'c'])
print(q)

q.append('d')
print(q)

q.appendleft('x')
print(q)



# defaultdict

    # 当直接读取 Dict 不存在的属性时，直接返回默认值

d1 = {'one':1, 'two':2, 'three':3}

print(d1['one'])
# print(d1['four'])  字典默认方法，访问不存的 key时，会报错



from collections import defaultdict

# lambda 表达式，直接返回字符串

func = lambda: 'hello'
d2 = defaultdict(func)

print(d2['one'])
print(d2['four'])


# Counter
    # 统计字会串个数

from collections import Counter
# 为什么下面结果不把abcdefgabced.....作为键值，而是以其中每一个字母作为键值
# 需要括号里内容为可迭代
c = Counter('shendlaxhatinghao')
print(c)


s = ["liudana", "love", "love", "love", "love", "wangxiaona"]
c = Counter(s)

print(c)