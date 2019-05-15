#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 图片的缩放、旋转、镜像等操作
from PIL import Image

ArwenIm =  Image.open('Arwen.jpg')

# 查看尺寸
print(ArwenIm.size)
width, height = ArwenIm.size   # 获取长和宽
quartersizedIM = ArwenIm.resize((int(width/2), int(height/2)))
# 长和宽都缩小一倍  resize 调整尺寸
quartersizedIM.save('ArwenQuartersized.jpg')   # 保存调整后的图片
print(quartersizedIM.size)

# 不按比例更改尺寸
sveltIm =  ArwenIm.resize((width, height+100))
sveltIm.save('ArwenSvelte.jpg')

# 图片旋转 默认方法图片长宽尺寸不动，多余部分裁切
ArwenIm.rotate(90).save('ArwenRotated90.jpg')
ArwenIm.rotate(180).save('ArwenRotated180.jpg')
ArwenIm.rotate(270).save('ArwenRotated270.jpg')

# 可用参数  expand=True
ArwenIm.rotate(90, expand=True).save('ArwenRotated270.jpg')

# 图片镜像操作
ThranduilIm = Image.open('Arwen.jpg')
ThranduilIm.transpose(Image.FLIP_LEFT_RIGHT).save('ThranduilHorizontal_flip.jpg')
ThranduilIm.transpose(Image.FLIP_TOP_BOTTOM).save('ThranduilHorizontal_top.jpg')
ThranduilIm.rotate(180).save('ArwenRotated180.jpg')