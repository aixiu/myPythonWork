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
    def __init__(self, name):
        self.name = name

a = Person('aixiu')
b = Person('ynxiu')

print(a.name, b.name)
print(a.x, b.x)

