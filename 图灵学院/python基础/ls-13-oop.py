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


# 构造函数
    # 在对象进行实例化的时候，系统自动调用的一个函数叫构造函数，
    # 通常此函数用来对实例对象进行初化工作。



# 构造函数例子

class Person(object):
    # 对person类进行实例化的时候
    # 姓名要确定，年龄得确定，地址要有
    def __init__(self):
        self.name = 'name'
        self.age = 18
        self.address = 'Studentuhonheim'
        print('In init func')

# 实例化一个人
p = Person()

# 构造函数的调用顺序
    # 如果子类没有写构造函数，则自动向上查找，直到找到位置

class A(object):
    def __init__(self):
        print('A')

class B(A):
    def __init__(self):
        print('B')

class C(B):
    pass

    # 此时，首先查找C的构造函数
    # 如果没有，则向上按照MRO顺序找父类的构造函数，只到找到为止。
c =C()


# 多态
    # 多态就是同一个对象在不同情况下有不同的状态出现
    # 多态不是语法，是一种设计思想。
    # 多态性：一种调用方式，有不同的执行效果
    # 多态：同一事物的多种形态，比如：动物分为人类，狗类，猪类

# Mixin 设计模式
    # 主要采用多继承方式对类的功能进行扩展

# 我们使用多继承语法来实现 Mixin
# 使用 Mixin实现多继承的时候需非常小心
    # 首先它必须表示某一单一功能，而不是某个物品
    # 职责必须单一，如果由多个功能，则写多个 Mixin
    # Mixin 不能依赖于子类实现
    # 子类即使没有继承这个 Mixin 类，也照样工作，只是缺少了某个功能

# 优点：
    # 使用 Mixin 可以在不对类进行任何修改的情况下，扩充功能
    # 可以方便的组织和维护不同功能组件的划分
    # 可以根据需要任意调整功能类的组合
    # 可以避免创建很多新的类，导致类的继承混乱

# Mixin 案例
class Person(object):
    name = 'liuying'
    age = 18

    def eat(self):
        print('Eat......')

    def drink(self):
        print('Drink......')

    def sleep(self):
        print('Sellp......')

class Teacher(Person):
    def work(self):
        print('Work......')

class Student(Person):
    def study(self):
        print('Study......')

class Tutor(Teacher, Student):
    pass

t = Tutor()
print(Tutor.__mro__)
print(t.__dict__)
print(Tutor.__dict__)

print('{:=^40}'.format('华丽的分割线'))

class TeacherMixin(object):
    def work(self):
        print('Work')

class StudentMixin(object):
    def study(self):
        print('Study')

class Tutorm(Person, TeacherMixin, StudentMixin):
    pass

tt = Tutorm()  # type: class

print(Tutorm.__mro__)
print(tt.__dict__)
print(Tutorm.__dict__)


# 类相关函数
    # issubclass: 检测一个类是否是另一个类的子类
    # isinstance: 检测一个对象是否是另一个类的实例
    # hasattr: 检测一个对象是否有成员XXX
    # getattr: get attribute
    # setattr: set attribute
    # delattr: delete attribute
    # dir: 获取对象的成员列表

# issbuclass 例子

class A(object):
    pass

class B(A):
    pass

class C(object):
    pass

print(issubclass(B, A))
print(issubclass(C, A))


# isinstance 例子
class A(object):
    pass

a = A()

print(isinstance(a, A))
print(isinstance(A, A))



# hasattr 例子
class A(object):
    name = 'NoName'

print(hasattr(a, 'name'))
print(hasattr(a, 'age'))


# help 案例
    # 我想知道 setattr 的具体用法

help(setattr)

# dir 案例
class A(object):
    pass

dir(A)
a =A()
dir(a)