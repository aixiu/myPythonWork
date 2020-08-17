#!/usr/bin/env python
# -*- coding: utf-8 -*-

## 文件操作示例

with open('test.txt', 'r', encoding='utf-8') as f:
    s = f.read()
    print(s)   

# with open('test.txt', 'a', encoding='utf-8') as f:
#     f.write('信不信有你')

from io import StringIO

f = StringIO()
f.write('hello')
f.write(' ')
f.write('world!')

print(f.getvalue())

# f = StringIO('Hello!\nHi!\nGoodbye!')
# f = StringIO('')
while True:
    s = f.readline()
    if s == '':
        break
    print(s.strip())


import os
import platform  # platform模块给我们提供了很多方法去获取操作系统的信息

print(os.name)
# print(os.uname())  # 注意uname()函数在Windows上不提供，也就是说，os模块的某些函数是跟操作系统相关的。
o = platform.uname()


print(o.system)
print(o.node)

# print(os.environ)
# 要获取某个环境变量的值，可以调用os.environ.get('key')：
print(os.environ.get('PATH'))
print(os.environ.get('x', 'default'))   #取X，设置默认值，如果没找到就抛出默认，默认值为：None


# 操作文件和目录

## 操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下。查看、创建和删除目录可以这么调用：

# 查看当前目录的绝对路径

print(os.path.abspath('.'))