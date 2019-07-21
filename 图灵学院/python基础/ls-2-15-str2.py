#!/usr/bin/env python
# -*- coding: utf-8 -*-

# format 格式化
    # 使用函数形式进行格式化，以代替以前的百分号

#不指定位置，按顺序读取
    # 方式一
s = '{} {}!'
print(s.format('Hello', 'world'))

    # 方式二
s = '{} {}!'.format('Hello', 'world')
print(s)

# 设置指定位置
s = '{0} {1}'.format('hello', 'world')
print(s)

# 使用命名参数
s = '我们的是{scholl_name},我们的网址是{url}'
s = s.format(scholl_name='图灵学院', url='www.baidu.com')
print(s)

# 通过字典设置参数，需要解包
    #使用命名参数
s = '我们的是{scholl_name},我们的网址是{url}'

s_dict = {'scholl_name':'图灵学院', 'url':'www.baidu.com'}

    # **是解包操作
s = s.format(**s_dict)
print(s)


# 对数字的格式化需要用到
s = 'liang is {:.2f}m heigh, {:.2f}KG weight'
print(s.format(1.84, 76.45))

    # ^ , <, >,分别是居中，左对齐，右对齐，后面带宽度。
    # ：号后面带填充字符，只能是一个字符，不指定则默认是用空格填充。
    # + 表示在正数前显示 + ，负数前显示 - ，（空格）表示在正数前加空格。
    # b, d, o, x 分别是二进制，十进制，八进制，十六进制。
    # 此外我们可以使用大括号 {} 来转义大括号。

# 大括号转义案例
s = 'format 函数是用{}来进行占位的'
print(s.format({}))

# str 内置函数
    # 很多语言字符串使用string表示，但是python用str表示字符串

