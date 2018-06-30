#!/usr/bin/env python
# -*- coding: utf-8 -*-

# message  统计单词出现的个数，如：Books:1  and:2 等。

import pprint
message = '''
Books and doors are the same thing books.
you open them, and you go through into another world.
'''

words = message.split()

count = {}

for word in words:    # 遍历列表每个值，用字典的方法查询，初始值设置为0，出现过一次累计 +1
    if not word[-1].isalpha(): # 如果列表中的字符串最后索引不是字母，那个，用word[:-1]丢弃
        word = word[:-1]

    word = word.lower()   # 把大写字母变为小写,只统计小写字符串。
    count.setdefault(word,0)
    count[word] += 1

pprint.pprint(count)
