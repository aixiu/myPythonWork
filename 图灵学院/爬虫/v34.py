#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
from bs4 import BeautifulSoup


url = 'http://www.baidu.com'

rsp = request.urlopen(url)
content = rsp.read()

soup = BeautifulSoup(content, 'lxml')

# bs自动转码  BeautifulSoup的格式化输出函数:prettify()
# content = soup.prettify()
# print(content)


# print('{:#^20}'.format('华丽的分割线'))
# print(soup.head)


print('{:#^20}'.format('华丽的分割线'))
print(soup.meta)
print('{:#^20}'.format('华丽的分割线'))
print(soup.link)
print(soup.link.name)
print(soup.link.attrs)
print(soup.link.attrs['type'])
soup.link.attrs['type'] = '量子广告'
print(soup.link)
print('{:#^20}'.format('华丽的分割线'))
print(soup.title)
print(soup.title.name)
print(soup.title.attrs)  # 属性空，所以显示{}
print(soup.title.string)
print('{:#^20}'.format('华丽的分割线'))
print(soup.name)
print(soup.attrs)


print('{:#^20}'.format('华丽的分割线'))
print(soup.name)
print('{:#^20}'.format('华丽的分割线'))
for i in soup.head.contents:
    if i.name == 'meta':
        print(i)
    if i.name == 'title':
        print(i.string)


print('{:#^20}'.format('华丽的分割线'))
tags = soup.find_all(name='meta')
print(tags)

import re
print('{:#^20}'.format('华丽的分割线'))
tags = soup.find_all(re.compile('^me'), content='always')
for tag in tags:
    print(tags)

print('{:#^20}'.format('华丽的分割线'))