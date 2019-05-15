#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 在画布上画图写字

from PIL import Image, ImageDraw   # ImageDraw模块提供了图像对象的简单2D绘制

# im = Image.new('RGBA', (200, 200), 'white')  # 生成一个图200*200的白色背景的图片对象
# draw = ImageDraw.Draw(im)   # 用Draw 函数对 IM 画画

# draw.line([(0,0), (199,0), (199,199), (0,199), (0,0)], fill='pink', width=10)
# # 第一个参数为一个列表，规定了线条的起点、路径和终点。fill 颜色 pink、线宽 10  
# draw.rectangle((20, 30, 60, 60), fill='blue')
# # 画矩形 第一参数为元组 前两个为左上角坐标，后两个为右下角的坐标  
# draw.ellipse((120, 30, 160, 60), fill='red')
# # 画一个内切于120，30与160，60，矩形的椭圆形
# draw.polygon(((57,87), (79,62), (94,85), (120,90), (103,113)), fill='brown', outline='green')
# # 画一个多边形，第一个参数为一个元素，outline 边框颜色

# for i in range(100,200,10):
#     draw.line([(i,0),(200,i-100)],fill='purple')

# im.save('drawing.png')

from PIL import ImageFont

#  在画布上写字

im = Image.new('RGBA', (200, 200), 'white')
draw = ImageDraw.Draw(im)   # 用Draw 函数对 IM 画画

draw.text((20,150), 'Hello', fill='purple')

SignPainterFont = ImageFont.truetype('impact.ttf', 32)  # 设定定体
# on Windows: c:\Windows\Fonts;  on os X: /Library/Fonts

draw.text((100,150), 'Howdy', fill='gray', font=SignPainterFont)
im.save('text.png')