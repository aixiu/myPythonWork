#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 安装Lxml
from lxml import etree

'''
用lxml来解析HTML代码
'''

text = '''
<div>
    <ul>
        <li class='item-0'><a href='0.html'>first item</a></li>
        <li class='item-1'><a href='1.html'>first item</a></li>
        <li class='item-2'><a href='2.html'>first item</a></li>
        <li class='item-3'><a href='3.html'>first item</a></li>
        <li class='item-4'><a href='4.html'>first item</a>
    </ul>
</div>
'''

# 利用etree.HTML把字符串解析成 HTML文档
# etree.HTML()可以用来解析字符串格式的HTML文档对象，将传进去的字符串转变成_Element对象

html = etree.HTML(text)

# etree.tostring()方法用来将_Element对象转换成字符串
# 调用tostring()方法即可输出修正后的HTML代码，
# 但是结果是bytes类型。这里利用decode()方法将其转成str类型

s = etree.tostring(html)

print(s.decode('utf-8'))