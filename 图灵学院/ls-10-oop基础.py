#!/usr/bin/env python
# -*- coding: utf-8 -*-

# oop - python 面向对象
    # 面向对象编程
        # 基础
        # 公有私有
        # 继承
        # 组合， Mixin
    # 魔法函数
        # 魔法函数概述
        # 构造类魔法函数
        # 运算类魔法函数

# 面向对象概述 （ObjectOriented.简称OO）
    # 任意一个任各，首先想到的是任务是由模型构成的。


# 类和对象的概念
    # 类：抽象名词，代表一个集合，共性的事物。
    # 对象：具体的事物，单个个体，是对象的一个实例。
    # 类和对象的关系
        # 一个具象，代表一类事物的某一个个体。
        # 一个是抽象，代表的一大类事物。

# 类中的内容，应该具体两个内容。
    # 事物的特征，叫做属性（变量）
    # 表明事物的功能或动作，称为成员方法（函数）

# 类的基本实现。
    # 类的命名
        # 遵守变量命名的规范
        # 大驼峰（由一个或多个单词构成，每个单词首字母大写，单词跟单词直接相连）
        # 尽量避开跟系统命名相似的命名

    # 类的声明
        # 必须用 class 关键字
        # 类由属性和方法构成，其他不允许出现
        # 成员属性定义可以直接使用。
    
    # 实例化类
        # 变量 = 类名()  实例化了一个对象

    # 访问对象成员
        # 使用点操作符
            # obj.成员属性名称
            # obj.成员方法

    # 可以通过默认内置变量检查类和对象所有的成员
        # 对象所有成员检查
            # obj.__dict__   dict 前后两个下划线
        # 类所有的成员
            # class_name.__dict__  dict 前后两个下划线

'''
定义一个学生类，用来形容学生
'''

# 一个代的类
class Student():
    # 一个空类，pass 代表直接跳过，此处 pass 必须有
    pass

# 定义一个对象
mingyue = Student()

# 再定一个类，用来描述听 python 的学生
class PythonStudunt(object):
    # 用 None 给不确定的值赋值
    name = None
    age = 18
    course = 'python'

    def doHomework(self):
        print('I 在做作业')

        # 推荐在函数末尾使用 return 语句
        return None

# 实例化 一个叫 yueyue 的学生，是一个具体的人
yueyue = PythonStudunt()
print(yueyue.name)
print(yueyue.age)

# 注意成员函数的调用没有传递进入参数
yueyue.doHomework()