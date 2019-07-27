#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Re 使用步骤

    # 1、使用compile 将表示正则的字符串编译为一个 pattern 对象
    # 2、通过 pattern对象提供一系列方法对文本进行查找匹配，获得匹配结果，一个Match 对象
    # 3、最后使用 Match 对象提供的属性和方法获得信息，根据需要进行操作。

# Re 常用函数

    # group(): 获得一个或者多个分组匹配的字符串， 当要获得整个匹配的子串时，直接使用 gourp或者 goup (0)
    # start: 获取分组匹配的子串在整个字符串中的起始位置，参数默认为0
    # end: 获取分组匹配的子串在整个字符串中的结束位置，默认为0
    # span:返回的结构技术(start (gourp), end (group))

# 导入相关包
import re

# 查找数字
    # r 表示字符串不转义
p = re.compile(r'\d+')     # 至少出现一次数字

# 在字符串 “one12towthree33456four78” 中进行查找，按照规则 P 制定的正则进行查找
# 返回结果是 None 青示没找到，否则会返回 match 对象
m = p.match('one12towthree33456four78')

print(m)


print('====================================')


# 导入相关包
import re

# 查找数字
    # r 表示字符串不转义
p = re.compile(r'\d+')     # 至少出现一次数字

# 在字符串 “one12towthree33456four78” 中进行查找，按照规则 P 制定的正则进行查找
# 返回结果是 None 青示没找到，否则会返回 match 对象
# 参数3， 6 表示字会串中查找的范围
m = p.match('one12towthree33456four78', 3, 26)

print(m)

# 上述代码说明的问题
    # 1、match 可以输入参数表示起始位置
    # 2、 查到的结果只包含一个，表示第一次进行匹配成功的内容

print(m[0])
print(m.start(0))
print(m.end(0))


print('===================================')

import re

# I 表示忽略掉大小写
p = re.compile(r'([a-z]+) ([a-z]+)', re.I)

m = p.match('I am really love wangxiaogjing')
print(m)
print(m.group(0))
print(m.start(0))
print(m.end(0))
print('================================')
print(m.group(1))
print(m.start(1))
print(m.end(1))
print('================================')
print(m.groups())



# 查找
    # search(str, [, pos[, endpos]])  
    # 在字符串中查找匹配，pos 和 endpos 表示起始位置

    # findall:查找所有
    # finditer：查找， 返回一个 iter 结果


print('================================')

import re
p = re.compile(r'\d+')

m = p.search('one12two34three567four')

print(m.group())


print('================================')

rst = p.findall('one12two34three567four')
print(type(rst))
print(rst)


# sub 替换的案例
    # sub(repl, str[, count])

print('================================')

import re

p = re.compile(r'(\w+) (\w+)')

s = 'hello 123 wang 456 xiangjing, i love you'

rst = p.sub(r'Hello world', s)

print(rst)



# 匹配中文
    # 大部分中文表示范围是 [u4e00-u9fa5], 不包括全角标点。

print('================================')

import re

title = u'世界 你好， hello moto'

p = re.compile(r'[\u4e00-\u9fa5]+')

rst = p.findall(title)

print(rst)


# 贪婪和非贪婪

    # 贪婪：尽可能多的匹配， （*）表示贪婪匹配
    # 非贪婪：找到符合条件的最小内容即可，（？）表示非贪婪
    # 正则默认使用贪婪匹配

print('================================')

import re 

title = u'<div>name</div><div>age</div>'

p1 = re.compile(r"<div>.*</div>")
p2 = re.compile(r"<div>.*?</div>")

m1 = p1.search(title)
print(m1.group())

m2 = p2.search(title)
print(m2.group())
