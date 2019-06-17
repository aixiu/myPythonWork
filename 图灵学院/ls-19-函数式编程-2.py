#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 系统高阶函数-map
    # 原意就是映射，即把集合或者列表的元素，每一个元素都按照一定规则进行操作，生成一个新的列表或者集合
    # map函数是系统提供的具有映射功能的函数，返回值是一个迭代对象

# map 举例
# 有一个列表，想对列表里的每个元素乘以10，并得到新的列表

l1 = [i for i in range(10)]

l2 = []
for i in l1:
    l2.append(i * 10)

print(l2)

# 利用map实现
def mulTen(n):
    return n * 10

l3 = map(mulTen, l1)
# map类型是一个可迭代的结构，所以可以使用for遍历
for i in l3:
    print(i)

# 以下列表生成式得到的结果为空， why？
l4 = [i for i in l3]
print(l4)


# reduce
    # 原意是归并，缩减
    # 把一个可迭代对象最后归并成一个结果
    # 对于作为参数的函数要求： 必须由两个参数，必须由返回结果
    # reduce([1,2,3,4,5]) == f( f(f(f(1,2),3), 4),5)
    # reduce 需要导入functools包

from functools import reduce

# 定义一个操作函数
# 加入操作函数只是相加
def myAdd(x,y):
    return x + y
    
# 对于列表[1,2,3,4,5,6]执行myAdd的reduce操作
rst = reduce( myAdd, [1,2,3,4,5,6] )
print(rst)