#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Student():   
    name = 'dana'
    age = 18

print(Student.__dict__)

yueyue = Student()
print(yueyue.__dict__)
print(yueyue.name)

# 类和对象的成员分析
    # 类和对象都可以存储成员，成员归类所有，也可以归对象所有
    # 类存储成员时使用的是与类关联的一个对象

# 创建对象的时候，类中的成员不会放入对象当中，而是得到一个空对象，没有成员
# 通过对象对类中成员重新赋值或者通过对象添加成员时，对应成员会保存在对象中，而不会修改类成员。


class A():
    name = 'dana'
    age = 18

    # 注意 say 的支，参数有一个 self
    def say(self):
        self.name = 'aaaa'
        self.age = 20

# 此时，A 称为类实例
print(A.name)
print(A.age)

print('*' * 20)

print(id(A.name))
print(id(A.age))

print('*' * 20)

a =A()

print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

print('*' * 20)

a.name = 'yaona'
a.age = 16
print(a.name)
print(a.age)
print(id(a.name))
print(id(a.age))

# 关于 self
    # self 在对象的方法中表示当前对象本身，如果通过对象调用一个方法，那么该对象会自动传入到当前方法的第一个参数中。
    # self 并不是关键字，只是一个用于接收对象的普通参数，理论上可以用任何一个普通变量代替

class Haha():
    name = 'dana'
    age = 18

    # 注意 say 的支，参数有一个 self
    def say(self):
        self.name = 'aaaa'
        self.age = 20
        print('My name is {}'.format(self.name))
        print('My age is {}'.format(self.age))

aixiu = Haha()
aixiu.say()


        # 方法中有 self 形参的方法成为非绑定类的方法，可以通过对象访问，没有 self 的是绑定类的方法。只能通过类方问
class Teacher(object):
    name = 'dana'
    age = 19

    def say(self):
        self.name = 'yaona'
        self.age = 17
        print('My name is {}'.format(self.name))
        print('My age is {}'.format(self.age))

    def sayAgain():        
        print('Hello, nice to see you again')

shen = Teacher()
shen.say()

# 调用绑定类函数使用类名
Teacher.sayAgain()

        # 使用类访问绑定类的方法时，如果类方法中需要访问当前类的成员，可以通过 __class__.成员名来访问
        # 如： __class__.name   __class__.age
    def sayAgain():
        # 调用类的成员变需要 __class__.变量名
        print(__class__.name)        
        print(__class__.age)        
        print('Hello, nice to see you again')

# 关于 self 的案例

class A(object):
    name = 'liuying'
    age = 18

    def __init__(self):
        self.name = 'aaaa'
        self.age = 200

    def say(self):
        print(self.name)
        print(self.age)

class B(object):
    name = 'bbbb'
    age = 90

# 此时，系统会默认把 a 作为第一个参数传入函数
a =A()
a.say()

# 此时， self 被 a 替换
A.say(a)
# 同样可以把A作为参数传入
A.say(A)

# 此时，传入的是类实例 B ，因为 B具有 name 和 age 属性，所以不会报错。
A.say(B)

# 以上代码，利用了鸭子模型，就是说，看起来是这个东西，然后用起来也具有这个东西的属性，那么我就认为就是这个东西，究竟是不是这个东西，我不关心。


# 面向对象的三大特性
    # 封装
    # 继承
    # 多态

# 封装
    # 封装就是对对象的成员进行访问限制
    # 封装的三个级别：
        # 公开， public
        # 受保护的，protected
        # 私有的，private
        # public, private, protedted 不是关键字

    # 判断对象的对置
        # 对象内部
        # 对象外部
        # 子类中

    # 私有
        # 私有成员是最高级别的封装，只能在当前类或对象中访问
        # 在成员前面添加两个下划线即可

# 私有变量案例
class Person(object):
    # name是共有的成员
    name = 'liuying'
    # __age 就是私有成员
    __age = 18

p = Person()
# name 是公有变量
print(p.name)
# __age 是私有变量
# 会报错，提示没有这个变量
print(p.__age)

        # python 的私有不是真私有，是一种叫 name mangling 的改名策略
        # 可以使用： 对象._classname_attr  访问
    
# name mangling 技术
print(p._Person__age)
    