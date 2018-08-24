#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import ImageColor  # 图片颜色模块 Pillow

# print('Red:{}'.format(ImageColor.getcolor('red', 'RGBA')))  # 大小写无关 ‘RGB’ 和 ‘rgb’
# print('Red:{}'.format(ImageColor.getcolor('RED', 'RGBA')))
# print('black:{}'.format(ImageColor.getcolor('black', 'RGBA')))

from PIL import Image

dollim = Image.open('doll.jpg')

print('Size:{}'.format(dollim.size))
width, height = dollim.size  # 把size 读取的数据 赋值给 长和宽
print('Width: {}\nHeight: {}'.format(width, height))  # 读取长和宽

print('Filename: {}'.format(dollim.filename))  # 读取文件名

print('Format: {}'.format(dollim.format))  #读取文件格式

print('Description: {}'.format(dollim.format_description))  # 文件的描述

dollim.save('doll_duplicate.png')   # 另存一个文件