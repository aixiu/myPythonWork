#!/usr/bin/env python
# -*- coding: utf-8 -*-

s = input('请输入一个数>>> ')
print('\n这是一个{}位数'.format(len(s)))

s = reversed(s)
print('\n{:=^30}\n'.format('个位，十位，百位，千位，万位的数字依次是'))

for i in s:    
    print('{}'.format(i))
