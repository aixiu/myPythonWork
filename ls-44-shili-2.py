#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 图片的缩放、旋转、镜像等操作
from PIL import Image

ArwenIm =  Image.open('.\Arwen.jpg')

# 查看尺寸
print(ArwenIm.size)