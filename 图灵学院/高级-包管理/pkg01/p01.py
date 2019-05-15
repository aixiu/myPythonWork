#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 包含一个学生类
# 一个 sayhello 函数
# 一个打印语句

class Student(object):
    def __init__(self, name='NoName', age=18):
        self.name = name
        self.age = age

    def say(self):
        print('My name is {}'.format(self.name))

def sayhello():
    print('Hi, 欢迎来到图灵学院！')
    

print('我是模块aaa.测试用的')