#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree


# 只能读取XMXL格式内容， html报错。
html = etree.parse(r'./图灵学院/爬虫/v30.xml')

print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)


# xpath 的意思是查找带有category属性值为sport的book元素
rst = html.xpath('//book[@category="sport"]')
print(type(rst))
print(rst)


# xpath 的意思是查找带有category属性值为sport的book元素下的year元素
rst = html.xpath('//book[@category="sport"]/year')
rst = rst[0]
print(type(rst))
print(rst.tag)
print(rst.text)