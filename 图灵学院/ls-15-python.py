#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 变量的三种用法

class A(object):
    def __init__(self):
        self.name = 'haha'
        self.age = 18

a =A
# 属性的三种用法
    # 赋值
    # 读取
    # 删除

a.name = '量子'
# del a.name
# print(a.name)

# 类属性 property
    # 应用场景
        # 对变量除了普通的三种操作，还想增加一些附加的操作，可以通过 PROPERTY完成

class A(object):
    def __init__(self):
        self.name = 'haha'
        self.age = 18

    # 此功能，是对类变量进行读取操作的时候执行函数功能
    def fget(self):
        print('我被读取了')
        return self.name

    # 模拟的是对变量进行写操作的时候执行的功能
    def fset(self):
        print('我被写入了，还有好多')
        self.name = '图灵学院'.format(name)

    # fdel 模拟的是删除变量的时候进行的操作
    def fdel(self):
        pass

    # property 的四个参数顺序是固定的
    # 第一个参数代表读取的时候需要调用函数
    # 第二个参数代表写入的进候需要调用的函数
    # 第三个是删除时需要调用的函数
    name2 = property(fget, fset, fdel, '这是一个properyt的例子')

a =A()
print(a.name)

print(a.name2)

# 抽象类
    # 抽象方法： 没有具体实现内容的方法成为抽象方法
    # 抽象方法的主要意义是规范了子类的行为和接口
    # 抽象的使用需要借助 abc 模块

# 抽象例子
class Animel(object):
    def sayHello(self):
        pass

class Dog(Animel):
    def sayHello(self):
        print('闻一下对方')

class Person(Animel):
    def sayHello(self):
        print('Kiss me')

d = Dog()
d.sayHello()

p = Person()
p.sayHello()

    # 抽象类：包含抽象方法的类叫抽象类，通常成为ABC类
    # 抽象类的使用：
        # 抽象类可以包含抽象方法，也可以包含具体方法
        # 抽象类中可以有方法，也可以有属性
        # 抽象类不允许直接实例化
        # 必须继承才可以使用，且继承的子类必须实现所有继承来的抽象方法
        # 假定，子类没有实所有继承的抽象方法，则子类也不能实例化
        # 抽象类的主要作用是设定类的标准备，以便于开发的时候具有统一的规范

# 抽象类的实现

import abc

# 声明一个类并且指定当前类的元类
class Human(metaclass=abc.ABCMeta):

    # 定义一个抽象方法
    @abc.abstractmethod
    def smoking(self):
        pass

    # 定义类抽象方法
    @abc.abstractclassmethod
    def drink():
        pass

    # 定义静态抽象方法
    @abc.abstractstaticmethod
    def play():
        pass

    def sleep(sefl):
        print('sleep...')


# 自定义类
    # 类其是一个类定义和各种方法的自由组合
    # 可以定义类和函数，然后自己能过类直接赋值
    # 借助于 MethodType 实现
    # 还可以借助于 type 实现
    # 利用元类实现 - MetaClass
        # 元类是类
        # 被用来创造别的类


# 函数名可以当变量使用

def sayHello(name):
    print('{}你好，来一发？'.format(name))

sayHello('月月')
liumang = sayHello

liumang('yueyue')






# 自己组装一个类

class A(object):
    pass

def say(self):
    print('Saying....')


say(9)
    
A.say = say
a = A()
a.say()


# 利用 type 造一个类


# 先定义类应该具有的成员函数 
def say(self):
     print('Saying...')

def talk(self):
    print('Talking...')

# 用 type 来创建类
A = type('AName', (object, ), {'class_say':say, 'class_talk':talk})

# 然后可以像正常访问一样使用类

a = A()
dir(a)


# 元类的例子
    # 元类写法是固定的，它必须继承自 type
    # 元类一般命名以 MetaClass结尾

class TulingMetaClass(type):
    # 注意以下写法    
    def __new__(cls, name, bases, attrs):
        #自己的功能
        print('哈哈，我是元类')
        attrs['id'] = '000000'
        attrs['addr'] = '湖北武汉'
        return type.__new__(cls, name, bases, attrs)

# 元类定义完成就可以使用，使用注意写法
class Teacher(object, metaclass=TulingMetaClass):
    pass

t = Teacher()
t.id