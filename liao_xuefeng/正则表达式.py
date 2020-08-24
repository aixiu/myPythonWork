#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re

test = '027-12345678'

if re.match(r'^\d{3}\-\d{3,8}$', test):
    print('OK')
else:
    print('failed')

test1 = '027 12345678'
if re.match(r'^\d{3}\s\d{3,8}$', test1):
    print('OK')
else:
    print('failed')


# 切分字符串
sta = 'p y  th on'
sta1 = 'p,y  th on'
sta2 = 'p,y ;;;th on'

print(re.split(r'\s+', sta))
print(re.split(r'\s+', sta1))
print(re.split(r'[\s\,]+', sta1))
print(re.split(r'[\s\,\;]+', sta1))

# 分组
m = re.match(r'^(\d{3})-(\d{3,8})$', test)
print(m.group(0))
print(m.group(1))
print(m.group(2))

m = re.match(r'^(\d{3})\s(\d{3,8})$', test1)
print(m.group(0))
print(m.group(1))
print(m.group(2))

# 例子：
t = '23:05:30'
m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
print(m.groups())

ss = '20'
s = re.match(r'^(0[0-9]|1[0-9]|[0-2])(0[0-9]|1[0-9]|[0-2])$', ss)
print(s.groups())