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
    age = 18
    __score = 0   # 私有的，只有自己能访问
    _petname = 'sec'  # 保护的，子类可以用，但不能公用
    def sleep(self):
        print('Sleeping ……')

# 继承父类写在括号内
class Teacher(Person):
    pass

t =Teacher()
print(t.name)

print(t._petname)
# 公开访问私有变量，报错。
# print(t.__score)

t.sleep()
# 继承的特征
    # 所有类都继承自 object 类，即所有类都是 object 类的子类
    # 子类一旦继承父类，则可以使用父类 除私有成员外的所有内容
    # 子类继承父类后并没有将父类成员完全赋值到子类中，而是通过引用关系访问调用
    # 子类中可以定义独有的成员属性和方法
    # 子类中定义的成员和父类成员如果相同，则优先使用子类的成员
    # 子类如果想扩充父类的方法，要吧在定义新方法的同时访问父类成员进行代码重用。
    # 可以使用 [父类名.父类成员]  的格式来调用父类成员，也可以用 [super().父类成员]的格式来调用

# 继承变量函数的查找顺序问题
    # 优先查找自己的变量
    # 没有则查找父类
    # 构造函数如果本类中没有定义，则自动查找调用父类构造函数
    # 如果本类有定义，则不在继续向上查找

# 什么是构造函数
    # 构造函数是一类特殊的函数，在类进行实例化之前进行调用。
    # 哪果定义了构造函数，则实例化时使用构造函数，不查找父类的构造函数
    # 如果没定义，则自动查找父类构造函数
    # 如果子类没定义，父类构造函数带参数，则构造对象时的参数应该按父类参数构造

# super 详解
    # super 不是关键字，而是一个类。
    # super 的作用是获取 MRO （MethodRseolustionOrder） 列表中的第一个类
    # super 于父类直接没有任何实质性关系，但是通过 super可以调用到父类
    # super 使用两个方法：参见在构造函数中调用父类 的构造函数

print(type(super))
# 输出 <class 'type'>






    # 继承中的构造函数 - 1

class Animel(object):
    pass

class PaxingAni(Animel):
    pass

class Dog(PaxingAni):
    # __init__  就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I am init in dog')

# 实例化的时候，括号内的参数需要跟构造函数匹配
kaka = Dog()


    # 继承中的构造函数 - 2

class Animel(object):
    def __init__(self):
        print('Animel')

class PaxingAni(Animel):
    def __init__(self):
        print('Paxing Dongwu')

class Dog(PaxingAni):
    # __init__  就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I am init in dog')

# 实例化的时候，括号内的参数需要跟构造函数匹配 ，自动调用了Dog的构造函数
# 因为找到了构造函数，则不会查找父类的构造函数
kaka = Dog()

# 猫没写构造函数
class Cat(PaxingAni):
    pass

#此时应该自动调用构造函数，因为 Cat 没有构造函数，所以查找父类的构造函数
# 在 PaxingAni 中查找到了构造函数，则停止向上查找
c = Cat()


    # 继承中的构造函数 - 3

class Animel(object):
    def __init__(self):
        print('Animel')

class PaxingAni(Animel):
    def __init__(self, name):
        print('Paxing Dongwu {}'.format(name))

class Dog(PaxingAni):
    # __init__  就是构造函数
    # 每次实例化的时候，第一个被自动调用
    # 因为主要工作是进行初始化，所以得名
    def __init__(self):
        print('I am init in dog')

# 实例化 Dog 时，查找到 Dog的构造函数，参数匹配，不报错
d = Dog()

class Cat(PaxingAni):
    pass

# 此时，由于Cat 没有构造函数，则向上查找
# 因为 PaxingAni 的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()



    # 继承中的构造函数 - 4

class Animel(object):
    def __init__(self):
        print('Animel')

class PaxingAni(Animel):
    pass

class Dog(PaxingAni):
    pass

# 实例化 Dog 时，查找到 Dog的构造函数，参数匹配，不报错
d = Dog()

class Cat(PaxingAni):
    pass

# 此时，由于Cat 没有构造函数，则向上查找
# 因为 PaxingAni 的构造函数需要两个参数，实例化的时候给了一个，报错
c = Cat()