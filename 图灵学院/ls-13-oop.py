#!/usr/bin/env python
# -*- coding: utf-8 -*-

    # 上接 ls-12-oop.py  上接 ls-12-oop.py  上接 ls-12-oop.py

class A(object):
    pass

class B(A):
    pass

# __mro__ 查看继承类的顺序
print(A.__mro__)
print(B.__mro__)


# 单继承和多继承
    # 单继承：每个类只能继承一个类
    #多继承：每个类允许继承多个类


# 单继承和多继承的优缺点
    # 单继承：
        # 优点：传承有序逻辑清晰语法简单隐患少
        # 缺点：功能不能无限扩展，只能在当前唯一的继承链中扩展
    # 多继承：
        # 优点：类的功能扩展方便
        # 缺点：继承关系很混乱

# 多继承的例子
    # 子类可以直接拥有父类的属性和方法，私有属性和方法除外

class Fish(object):
    def __init__(self, name):
        self.name = name
    def swim(self):
        print('i am swimming ....')

class Bird(object):
    def __init__(self, name):
        self.name = name
    def fly(self):
        print('i am flying ....')

class Person(object):
    def __init__(self, name):
        self.name = name

    def workd(self):
        print('Working ....')

class SuperMan(Person, Bird, Fish):
    def __init__(self, name):
        self.name = name


s = SuperMan('yueyue')
s.fly()
s.swim()

# 单继承的例子
class Student(Person):
    def __init__(self, name):
        self.name = name

stu = Student('yueyue')
stu.workd()


# 菱形继承/钻石继承的问题
    # 多个子类继承自同一个父类，这些子类又被同一个类继承，于是继承关系图形成一个菱形图谱
    # 关于多继承的 MRO
        # MRO 就是多继承中，用于保存继承顺序的一个列表
        # python 本身采用 C3 算法来计算类继承的菱形继承进行计算的结果
        # MRO 列表的计算原则：
            # 子类永远在父类前面
            # 如果多个父类，则根据继承语法中括号内类的书写顺序存放
            # 如果多个类继承了同一个父类，孙子类中只会选取继承语法括号中第一父类的父类


# 菱形继承问题案例：

class A(object):
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass