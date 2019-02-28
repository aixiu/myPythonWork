#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数文档
# 文档查看方法一： 使用 hellp 函数，如：help(list)
# 文档查看方法二： 使用 __doc__。

def stu(name, age, *args, **kwargs):
    '''
    第一行文档
    第二行文档
    第三行文档
    '''
    print('This is hanshu stu')

#查看函数文档
print(help(stu))
print(stu.__doc__)