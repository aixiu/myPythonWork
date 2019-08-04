#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
python 中正则模块是 re
使用步骤：
1、compile 函数将正则表达式的字符串编译为一个pattern对象
2、通过 pattern 对象的一系列方法对文本进行匹配，匹配结果是一个 match 对象
3、用 Match 对象的方法，对结果进行操作
'''

import re

# \d表示一个数字
# 后面的+号表示这个数字可以出现一次或者多次，不允许出现0次
# r就是不转义，就是显示原生态

s = r'\d+'

#  返回一个 Pattern对象
# 默认找到一个就返回
pattern = re.compile(s)

# 返回一个 Match 对象
m = pattern.match('one12two2three2')

print(type(m))
# 默认匹配从头部开始，所以此次结果为 None
print(m)


# 返回一个 Match 对象
# 后面为位置参数含义是从哪个位置开始查找
m = pattern.match('one12two2three2', 3, 10)

print(type(m))
# 默认匹配从头部开始，所以此次结果为 None
print(m)

# .group()把找到找内容显示出来
print(m.group())
print(m.start(0))
print(m.end(0))
print(m.span(0))