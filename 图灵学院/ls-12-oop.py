#!/usr/bin/env python
# -*- coding: utf-8 -*-

    # 上接 ls-11-oop.py  上接 ls-11-oop.py  上接 ls-11-oop.py

    # 受保护的封装 protected
        # 受保护的封装是将对象成员进行一定级别的封装，然后，在类中或者子类中都可以进行访问，但是在外部不可以
        # 封装方法： 在成员名称前添加一个下划线即可

        # 常用属性定义
        # class Programer(object):
        #     def __init__(self, name, age, weight):
        #         self.name = name   # 可以公开访问（没带下划线）
        #         self._age = age    # 一般代表类的私有属性（一个下划线）
        #         self.__weight = weight   # 部分私有属性（二个下划线）

    # 公开的，公共的 public
        # 公共的封装实际对成员没有任何操作，任何地方都可以访问
# 继承
    # 继承就是一个类可以获得另一个类中的成员属性和成员方法
    # 作用：减少代码，增加代码的复用性，同时可以设置类与类直接的关系
    # 继承与被继承的概念：
        # 被继承的类叫：父类，也叫基类，也叫超类
        # 用于继承的类叫：子类也叫上派生类
        # 继承与被继承一定存在一个 is a 的关系，

# 继承的语法
    # 在 python 中任何类都有一个共同的父类叫 object
class Person(object):
    name = 'NoName'
    age = 0
    def sleep(self):
        print('Sleeping ……')

# 继承父类写在括号内
class Teacher(Person):
    pass

t =Teacher()
print(t.name)
print(Teacher.name)

# 继承的特征
    # 所有类都继承自 object 类，即所有类都是 object 类的子类
    # 子类一旦继承父类，则可以使用父类 除私有成员外的所有内容
    # 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    # 子类中可以定义独有的成员属性和方法
    # 子类中定义的成员和父类成员如果相同，则优先使用子类的成员
