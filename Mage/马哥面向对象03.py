#!/usr/bin/env python
# -*- coding: utf-8 -*-

class MyClass(object):
    xxx = 'XXX'

    def foo(self):
        print('foo')

    @classmethod
    def clsmtd(cls):
        print('{}.xxx = {}'.format(cls.__name__, cls.xxx))

    @staticmethod
    def staticmtd():
        print('static')

a = MyClass()
a.foo()

print(MyClass.__dict__)

MyClass.clsmtd()
a.clsmtd()  #  a.__class__.clsmtd()

MyClass.staticmtd()
a.staticmtd()