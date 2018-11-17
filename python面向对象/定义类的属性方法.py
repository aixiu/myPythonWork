#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 直接在类里定义
# class Programer(object):
#     sex = 'male'

# 在构造函数里定义
# class Programer(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# 常用属性定义
# class Programer(object):
#     def __init__(self, name, age, weight):
#         self.name = name   # 可以公开访问（没带下划线）
#         self._age = age    # 一般代表类的私有属性（一个下划线）
#         self.__weight = weight   # 部分私有属性（二个下划线）

# 实例说明
class Programer(object):
    '这是一个帮助信息'   #类文档字符串
    hobby = 'Play Computer'

    def __init__(self, name, age, weight):
        self.name = name
        self._age = age
        self.__weight = weight

    def get_weight(self):
        return self.__weight

if __name__ == '__main__':
    programer = Programer('Albert', 25, 80)
    print(dir(programer))
    print(programer.__dict__)
    print(programer.get_weight())
    print(programer._Programer__weight)


# 函数是直接用函数名调用的，方法是类的一部分，依附于一个类，


print(Programer.__doc__)