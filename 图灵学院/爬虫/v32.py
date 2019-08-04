#!/usr/bin/env python
# -*- coding: utf-8 -*-

from lxml import etree


# 只能读取XMXL格式内容， html报错。
html = etree.parse(r'./图灵学院/爬虫/v30.xml')

print(type(html))

rst = html.xpath('//book')
print(type(rst))
print(rst)
