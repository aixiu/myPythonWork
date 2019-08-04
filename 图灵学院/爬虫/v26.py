#!/usr/bin/env python
# -*- coding: utf-8 -*-

# search 的练习

import re

s = r'\d+'

pattern = re.compile(s)

m = pattern.search('one12two34three56')
print(m.group())

#  参数表明搜索的开始范围
m = pattern.search('one12two34three56', 10, 40)
print(m.group())


print('****************************')
# findall 的练习

import re

pattern = re.compile(r'\d+')

s = pattern.findall('i am 18 years old and 180 high')
print(s)


print('****************************')
# finditer 的练习

import re

pattern = re.compile(r'\d+')

s = pattern.finditer('i am 18 years old and 180 high')
print(type(s))

for i in s:
    print(i.group())