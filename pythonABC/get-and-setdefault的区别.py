#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 字典的 .get()  和 .setdefault函数  区别。

dict.get(key,default=’None’)
返回指定键的值，如果值不在字典中返回default值

>>>d={}
>>>d.get('name','N/A')
'N/A'
>>>d
{}
>>>print d.get('name')
None
>>>d
{}

可见使用get函数前后d的键值对数量不变

dict.setdefault(key,default=’None’
>>>d={}  #part1
>>>d.setdefault('name','N/A')
'N/A'
>>>d
{'name':'N/A'} 
>>>d.setdefault('name','Jack')
'N/A'
>>>d={}  #part2
>>>d.setdefault('name')
>>>d
{'name':'None'}

# 可以看到，当键不存在的时候，setdefault函数返回默认值并且相应地更新字典。
# 如果键存在，那么就返回与其对应的值，但不改变字典。默认值是可选的，这点和get一样。
# 如果不设定，默认使用None。