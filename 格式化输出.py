#!/usr/bin/env python
# -*- coding: utf-8 -*-


name = "毛毛"
print("%s, 今天你开心嘛!" % name)  # 第一种 % 号：

print("{0}, 今天你开心嘛".format(name))  # 第一种 format 号：

print(f"{name}, 今天你开心嘛!")  # f-字符串格式化


# 注：
# 第一种 与c语言的printf()函数相似 采用%传入参数
# % 后实质上是元组，可以元组的方式传入多个参数。

# 第二种 Python2.6 新增了一种格式化字符串的函数 str.format()
# {}内数字可以省略，数字可以选择传入的参数的顺序

# 第三种 Python3.6 新增了一种f-字符串格式化 运行时使用format()协议进行格式化


# 常用：

print('\n{:=^40}\n'.format('华丽的分割线'))
print(f'10年后共有: {money:.2f}')


# 格式化字符串的4种方式

''' 
目录：
Python格式化字符串的4中方式
一：%号
二：str.format
三：f-Strings
四：标准库模板
五：总结四种方式的应用场景

'''

# Python格式化字符串的4种方式
# 一：%号
# ​ %号格式化字符串的方式从Python诞生之初就已经存在，时至今日，python官方也并未弃用%号，但也并不推荐这种格式化方式。

# 1、格式的字符串（即%s）与被格式化的字符串（即传入的值）必须按照位置一一对应
# ps：当需格式化的字符串过多时，位置极容易搞混
print('%s asked %s to do something' % ('egon', 'lili'))  # egon asked lili to do something
print('%s asked %s to do something' % ('lili', 'egon'))  # lili asked egon to do something

# 2、可以通过字典方式格式化，打破了位置带来的限制与困扰
print('我的名字是 %(name)s, 我的年龄是 %(age)s.' % {'name': 'egon', 'age': 18})

kwargs={'name': 'egon', 'age': 18}
print('我的名字是 %(name)s, 我的年龄是 %(age)s.' % kwargs)


# 二：str.format
# ​ 该format方法是在Python 2.6中引入的，是字符串类型的内置方法。因为str.format的方式在性能和使用的灵活性上都比%号更胜一筹，所以推荐使用

# 2.1 使用位置参数

# 按照位置一一对应
print('{} asked {} to do something'.format('egon', 'lili'))  # egon asked lili to do something
print('{} asked {} to do something'.format('lili', 'egon'))  # lili asked egon to do something

# 2.2 使用索引

# 使用索引取对应位置的值
print('{0}{0}{1}{0}'.format('x','y')) # xxyx
2.3 使用关键字参数or字典

# 可以通过关键字or字典方式的方式格式化，打破了位置带来的限制与困扰
print('我的名字是 {name}, 我的年龄是 {age}.'.format(age=18, name='egon'))

kwargs = {'name': 'egon', 'age': 18}
print('我的名字是 {name}, 我的年龄是 {age}.'.format(**kwargs)) # 使用**进行解包操作
2.4 填充与格式化

# 先取到值,然后在冒号后设定填充格式：[填充字符][对齐方式][宽度]

# *<10：左对齐，总共10个字符，不够的用*号填充
print('{0:*<10}'.format('开始执行')) # 开始执行******

# *>10：右对齐，总共10个字符，不够的用*号填充
print('{0:*>10}'.format('开始执行')) # ******开始执行

# *^10：居中显示，总共10个字符，不够的用*号填充
print('{0:*^10}'.format('开始执行')) # ***开始执行***
2.5 精度与进制

print('{salary:.3f}'.format(salary=1232132.12351))  #精确到小数点后3位，四舍五入，结果为：1232132.124
print('{0:b}'.format(123))  # 转成二进制，结果为：1111011
print('{0:o}'.format(9))  # 转成八进制，结果为：11
print('{0:x}'.format(15))  # 转成十六进制，结果为：f
print('{0:,}'.format(99812939393931))  # 千分位格式化，结果为：99,812,939,393,931


# 三：f-Strings
# str.format() 比 %格式化高级了一些，但是它还是有自己的缺陷。当需要传入的字符串过多时，仍然会显得非常冗长。与在Python 3.6中引入 了f-strings，不仅比str.format更简洁，性能上也更胜一筹

# ​ f-string是以f或F开头的字符串， 核心在于字符串中符号{}的使用

# 3.1 {}中可以是变量名

name = 'egon'
age = 18
print(f'{name} {age}')  # egon 18
print(F'{age} {name}')  # 18 egon
3.2 {}中可以是表达式

# 可以在{}中放置任意合法的Python表达式，会在运行时计算
# 比如：数学表达式
print(f'{3*3/2}') # 4.5

# 比如：函数的调用
def foo(n):
    print('foo say hello')
    return n

print(f'{foo(10)}') # 会调用foo(10),然后打印其返回值

# 比如：调用对象的方法
name='EGON'
print(f'{name.lower()}') # egon

# 3.3 在类中的使用

''' 
>>> class Person(object):
...     def __init__(self, name, age):
...         self.name = name
...         self.age = age
...     def __str__(self):
...         return f'{self.name}:{self.age}'
...     def __repr__(self):
...         return f'===>{self.name}:{self.age}<==='
... 
>>> 
>>> obj=Person('egon',18)
>>> print(obj) # 触发__str__
egon:18
>>> obj        # 触发__repr__
===>egon:18<===
>>> 
>>> 
>>> 
>>> # 在f-Strings中的使用
>>> f'{obj}'   # 触发__str__
'egon:18'
>>> f'{obj!r}' # 触发__repr__
'===>egon:18<===' 
'''

# 3.3 多行f-Stings

# 当格式化字符串过长时，如下列表info
name = 'Egon'
age = 18
gender = 'male'
hobbie1='play'
hobbie2='music'
hobbie3='read'
info = [f'名字：{name}年龄：{age}性别：{gender}',f'第一个爱好：{hobbie1}第二个爱好：{hobbie2}第三个爱好：{hobbie3}'] 

# 我们可以回车分隔到多行，注意每行前都有一个f
info = [
    # 第一个元素
    f'名字：{name}'
    f'年龄：{age}'
    f'性别：{gender}',

    # 第二个元素
    f'第一个爱好：{hobbie1}'
    f'第二个爱好：{hobbie2}'
    f'第三个爱好：{hobbie3}'
]

print(info)
# ['名字：Egon年龄：18性别：male', '第一个爱好：play第二个爱好：music第三个爱好：read']

# 3.4 引号的嵌套

# 当字符串嵌套发送冲突时，与正常的字符串处理方式是一样的
# 1、外层为单引号，内层嵌套也为单引号，并且想要输入的内容也为单引号，那么外层需要改用双引号
print("my name is 'egon'")

# 2、外层为单引号，内层嵌套也为单引号，并且想要输入的内容也为单引号，需要用到转义
print('my name is \'egon\'')

# 3.5注意

#1、反斜杠可以用来进行字符转义，但不能用在{}的表达式中
f'{1\2}' # 语法错误

#2、注释#号也不能出现在{}的表达式中
f'{x#}' # 语法错误

# 3.6 括号的处理

# 基于3.5我们得知，不能在{}内出现反斜杠\，所以，当我们的输出的结果中需要包含{}时，下面的做法就是错误的

print(f'\{天王盖地虎\}')
类似于输出%号的做法

''' 
>>> print('%s%%' %30)
30% 
'''

# 若想输出{},那么需要在原有的基础上再套一层，如下

print(f'{{天王盖地虎}}') # {天王盖地虎}

print(f'{{{{天王盖地虎}}}}') # {{天王盖地虎}}


# 性能对比=>f_Stings性能最高

from timeit import timeit


def test_s():
    name = 'Egon'
    age = 18
    return '%s:%s.' % (name, age)


def test_format():
    name = 'Egon'
    age = 18
    return '{}:{}.'.format(name, age)


def test_f_strings():
    name = 'Egon'
    age = 18
    return f'{name}:{age}.'


res1 = timeit(test_s, number=1000000)
res2 = timeit(test_format, number=1000000)
res3 = timeit(test_f_strings, number=1000000)
print(res1) # 0.3709844550030539
print(res2) # 0.47834375899401493
print(res3) # 0.3111891380031011, 最快


# 四：标准库模板
# ​ 从Python 2.4起，Python标准库string引入了Template也可以用来格式化字符串，所以说，与前三种方式的一个显著区别就是：Template并属于python语言的核心语法特征，使用方式如下

from string import Template

name='EGON'
t = Template('Hello $name!')
res=t.substitute(name=name)

print(res)  # Hello EGON!

# 另外一个不同的地方是这个模板字符串不支持类似str.format那样的进制转换，需要我们自己处理

from string import Template

name='EGON'
templ_string = 'Hello $name, there is a $error error!!!'
res=Template(templ_string).substitute(name=name, error=hex(12345))

print(res) # Hello EGON, there is a 0x3039 error!!!

# 使用模板字符串Template的最佳的时机就是当你的程序需要处理由用户提供的输入内容时。模板字符串是最保险的选择，因为可以降低复杂性。

# 其他一些复杂的字符串格式化技巧的可能会给你的程序带来安全漏洞


''' 
五：总结四种方式的应用场景
1、如果格式化的字符串是由用户输入的，那么基于安全性考虑，推荐使用Template

2、如果使用的python3.6+版本的解释器，推荐使用f-Stings

3、如果要兼容python2.x版本的python解释器，推荐使用str.format

4、如果不是测试的代码，不推荐使用% 
'''