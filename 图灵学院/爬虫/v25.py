#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
正则结果Match 的使用案例
正则表达式可以包含一些可选标志修饰符来控制匹配的模式。
修饰符被指定为一个可选的标志。多个标志可以通过按位 OR(|) 它们来指定。
如 re.I | re.M 被设置成 I 和 M 标志：

修饰符	描述
re.I	使匹配对大小写不敏感
re.L	做本地化识别（locale-aware）匹配
re.M	多行匹配，影响 ^ 和 $
re.S	使 . 匹配包括换行在内的所有字符
re.U	根据Unicode字符集解析字符。这个标志影响 \w, \W, \b, \B.
re.X	该标志通过给予你更灵活的格式以便你将正则表达式写得更易于理解。

参考：https://www.cnblogs.com/feifeifeisir/p/10627474.html
'''

import re
# 以下正则分成了两个组，以小括号为单位
s = r'([a-z]+) ([a-z]+)'

pattern = re.compile(s, re.I) #  s.I表示忽略大小写

m = pattern.match('Hello world wide web')

# grout(0) 表示返回匹配成功的整个字串
s = m.group(0)
print(s)

a = m.span(0)   # 返回匹配成功的整个子串的跨度
print(a)

# gorup(1)  表示返回的第一个分组匹配成功的子串
s = m.group(1)
print(s)

# #返回匹配成功的第一个个子串的跨度
a = m.span(1)   # 返回匹配成楞的整个子串的跨度
print(a)

# gorup()  等阶于 m.gourp(1),m.gourp(2).....
s = m.groups()
print(s)
