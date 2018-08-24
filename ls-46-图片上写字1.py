#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在画布上画图写字

from PIL import Image

im = Image.new('RGBA', (100,100))
# 生成一个图片 颜色系 RGB  200宽 100高 ，如果不设置颜色，则生成一个透明的图片
print('transparent background: {}'.format(im.getpixel((0, 0))))
# getpixel，该函数检索指定坐标点的像素的RGB颜色值。 生成的颜色为：R,G,B,透明度

for x in range(100):
    for y in range(50):
        im.putpixel((x, y), (20, 165, 210))   
        # 将颜色 (20, 165, 210) 填充 X，Y  只能给颜色色值，不能给颜色名字

from PIL import ImageColor

for x in range(100):
    for y in range(50,100):
        im.putpixel((x, y), ImageColor.getcolor('violet', 'RGBA'))
        # ImageColor.getcolor 可以直接给定颜色名字，

print('上半部分颜色>>> {}'.format(im.getpixel((0, 0))))
print('下半部分颜色>>> {}'.format(im.getpixel((0, 50))))

im.save('putPixel.png')   # 生成图片