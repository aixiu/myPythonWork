#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类的成员描述符（属性）

    # 类的成员描述符是为了在类中对类的成员属性进行相关操作而创建的一种方式
        # get: 获取属性的操作
        # set: 修改或者添加属性的操作
        # delete: 删除属性的操作

    # 如果想使用类的成员描述符，大概有三种方法：
        # 使用类实现描述器
        # 使用属性修饰符
        # 使用 property 函数
            # property函数很简单
            # property(fget, fset, fdel, doc)

# 属性案例
    # 创建 Student 类，描述学生灰
    # 学生具有 Studen.name 属性
    # 但 name 格式并不统一
    # 可以用增加一个函数，然后自动调用的方式，但很蠢

class Student(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 如果不想修改代码
        self.setName(name)

    def intro(self):
        print('Hai, my name is {}'.format(self.name))

    def setName(self, name):
        self.name = name.upper()

s1 = Student('LIU Ying', 19.8)
s2 = Student('michi stangle', 24.0)

s1.intro()
s2.intro()


# property函数案例

    # 定义一个 Person 类，具有 name, age 属性
    # 对于任意输入的姓名，我们希望都用大写方式保存
    # 年龄，我们希望内部统一用整数保存
    # x = property(fget, fset, fdel, doc)

class Person(object):
    '''
    这是一个人，一个高尚的人，一个脱离了低级趣味的人
    '''
    # 函数的名称可以任意
    def fget(self):
        return self._name * 2

    def fset(self, name):
        # 所有输入的姓名以大写形式保存
        self._name = name.upper()

    def fdel(self):
        self._name = 'NoName'

    name = property(fget, fset, fdel, '对name进行下操作啦')

p1 = Person()
p1.name = 'TuLing'
print(p1.name)

# 无论哪种修饰符都是为了对成员属性进行相应的控制
    # 类的方式：适合多个类中的多个属性共用一个描述符
    # property：使用当前类中使用，可以控制一个类中多个属性
    # 属性修饰符：使用于当关类中使用，控制一个类中的一个属性


# 类的内置属性

    # __dict__：以字典的方式显示类的成员组成
    # __doc__：获取类的文档信息
    # __name__： 获取类的名称，如果在模块中使用，获取模块名称
    # __bases__：获取某个类的所有父类，以元组的方式显示


# 类的内置属性例子

print(Person.__dict__)
print(Person.__doc__)
print(Person.__name__)
print(Person.__bases__)


# 类的常用魔术方法
    # 魔术方法就是不需要人为调用的方法，基本是在特定的时刻自动触发
    # 魔术方法的统一特征，方法名被前后各两个下划线包裹
    # __init__：构造函数
    # __new__: 对象实例化方法，此函数罗特殊，一般不需要使用
    # __call__： 对象当函数使用的时候触发
    # __str__：当对象被当做字符器具吏用的时候调用
    # __repr__：返回字符串

# init 举例

class A(object):
    def __init__(self, name=0):
        print('哈哈，我被调用了')

a = A()


# __call__举例

class A(object):
    def __init__(self, name=0):
        print('哈哈，我被调用了')

    # __call__： 对象当函数使用的时候触发
    def __call__(self):
        print('我又被调用了一次')

a = A()
a()   # a 对象当作函数来用



# __str__举例

class A(object):
    def __init__(self, name=0):
        print('哈哈，我被调用了')

    # __call__： 对象当函数使用的时候触发
    def __call__(self):
        print('我又被调用了一次')

    # __str__：当对象被当做字符使用的时候调用，返回一个字符串
    def __str__(self):
        return '图灵学院的例子'

a = A()
print(a)  # a 对象当作函数来用

# 描述符相关
    # __set__:
    # __get__:
    # __delete__:

# 属性操作相关
    # __getattr__： 访问一个不存的属性时触发
    # __setattr__： 对成员属性进行设置的时候触发
        # 参数：
            # self用来获取当前对象
            # 被设置的属性名尔，以字符串形式出现
            # 需要对属性名称设置的值
        # 作用：
            # 进行属性设置的时候进行验证或者修改
        # 注意：在该方法中不能对属性直接进行赋值操作，否则死循环

# __getattr__ 例子
class A(object):
    name = 'NoName'
    age = 18

    # 哪果访问的属性不存在，则执行下边操作
    def __getattr__(self, name):
        print('没找到啊没找到')
        print(name)
        # return '返回值'

a = A()
print(a.name)
print(a.addr)


# __setattr__ 案例
class Person(object):
    def __init__(self):
        pass
    
    def __setattr__(self, name, value):
        print('设置属性：{}'.format(name))

        # 下面语句会导致问题，死循环
        # self.name = value
        # 为了避免死循环，规定统一敞露用父类魔法函数
        super().__setattr__(name, value)

p = Person()
print(p.__dict__)
p.age = 18