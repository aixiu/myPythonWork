#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://ke.qq.com/webcourse/index.html#cid=134017&term_id=100150034&taid=1982462414687105&type=512&vid=i1424rvc2vo
# 实例化讲解

# class Person(object):
#     def __init__(self):
#         self.name = 'tom'

# a = Person()
# b = Person()

# print(a.name, b.name)


class Person(object):
    x = 'abc'
    def __init__(self, name, age = 18):
        self.name = name
        self.y = age
        # 注意，__init__()  方法不能有返回值，也就是只能是None 

    def show(self):
        print(self.name, self.y)

a = Person('aixiu')
b = Person('ynxiu', 27)

print(a.name, b.name)
print(a.x, b.x)

print(a.y, b.y)

a.show()