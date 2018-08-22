#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 正则表达式学习记录。

import re

# m = re.match('abc', 'abcdef')
# m = re.match('[0-9]', '4815563abcdef')
# m = re.match('[0-9][0-9]', '4815563abcdef')
# m = re.match('[0-9]{0,10}', '4815563abcdef')
# m = re.match('[0-9]{10}', '4815563abcdef')

# m = re.findall('[0-9]{1,10}', '4815563abc96def')
# 如果被查找的字符串开头，中间，或是其它的不相连的地方都有数字，
# 那么，用 re.findall 方法查找，且只能用print(m)查看


# print(m)    # 查看匹配结果，无具体内容。如果匹配显示 'objec',否则显示'None'
# print(m.group())    # 查看匹配到的具体内容



# 注意： 
# .match() 方法，是从头开始匹配
# [0-9]只是匹配一个数字，如果想匹配多个可以 [0-9][0-9]这样。
# 当然，也可以用 [0-9]{0,10} `{}`中是指，把[0-9]匹配 0-10 次。
# 如果{10}，就是直接匹配 10次，如果被匹配的数字小于10个，那么侧匹配不上。


string = '192.168.2.49'

m = re.match('([0-9]{1,3}\.){3}\d{1,3}', string)

print(m.group())