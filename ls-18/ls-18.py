#!/usr/bin/env python
# -*- coding: utf-8 -*-

picnicItems = {'apple':5, 'cup':10}
picnicItems['bacon'] = 7

print(picnicItems)
print()


# .setdefault() 如果字典中包含有给定键，则返回该键对应的值，否则返回为该键设置的值
# dict = {'runoob': '菜鸟教程', 'google': 'Google 搜索'}
 
# print "Value : %s" %  dict.setdefault('runoob', None)
# print "Value : %s" %  dict.setdefault('Taobao', '淘宝')

# 以上实例输出结果为：
# Value : 菜鸟教程
# Value : 淘宝

picnicItems.setdefault('sausage',0)
print(picnicItems)
print()

picnicItems.setdefault('apple',3)
print(picnicItems)
print()

print('We have {} apples and {} eggs'.format(picnicItems.get('apple',0),picnicItems.get('eggs',0)))

