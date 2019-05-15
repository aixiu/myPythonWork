#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PIL import Image

# # 生成一个图片
# im = Image.new('RGBA',(200, 100), 'purple')  
# # 生成一个图片 颜色系 RGB  200宽 100高 ，颜色为：purple 紫色
# im.save('purpleImage.png')  # 把生成的图片保存

# im2 = Image.new('RGBA',(200, 100))  
# # 如果不设置颜色，则生成一个透明的图片
# im2.save('purpleImage-1.png')  # 把生成的图片保存

# #图片的剪切操作
# dollIm = Image.open('doll.jpg')
# croppendIm =  dollIm.crop((72,2,382,289))   # (72,2,382,289)为坐标，前两个左上，后两个右下
# croppendIm.save('cropped.jpg')  # 保存图片结果

# #复制粘贴操作
# dollCopyIm = dollIm.copy()    # 新建一个复制图片对象

# dollCopyIm.paste(croppendIm, (0, 0))  # 在新图片对象里把上边剪切后的对象放进去，起点为（0，0）
# dollCopyIm.paste(croppendIm, (300, 300))

# dollCopyIm.save('pasted.jpg') # 保存图片

# #复制粘贴操作二，透明背景图片
# reindeerIm = Image.open('reindeer.png') # 打开一个透明背景图片
# dollCopyIm.paste(reindeerIm, (10, 10), reindeerIm)
# # 把这个透明图片粘贴到dollCoppyIM对象的图片中去，如果不加reindeerIm对象名，出现图色背景，反之黑色背景
# dollCopyIm.save('transparentBackground.jpg')

# 图片加水印
hotaAirBalloonIm = Image.open('liangzi.png')
hotaixiuIm = Image.open('doll.jpg')
hotAirBalloonCopy = hotaAirBalloonIm.copy()   # 复制一份小图
hotaixiuCopy = hotaixiuIm.copy()   # 复制一份大图

hotaixiuCopyWidth, hotaixiuCopyHight = hotaixiuCopy.size    # 大图的宽和高
hotaAirBalloonCopyWith, hotAirBalloonCopyHight = hotAirBalloonCopy.size  # 水印小图的宽和高


for left in range(0, hotaixiuCopyWidth, hotaAirBalloonCopyWith):   # 在大图的宽度内，步长为小图的宽度
    for top in range(0, hotaixiuCopyHight, hotAirBalloonCopyHight):  # # 在大图的高度内，步长为小图的高度
        hotaixiuCopy.paste(hotAirBalloonCopy, (left, top))    # 把水印小图在上边取得的范围内贴满

hotaixiuCopy.save('tiled.jpg')  # 保存为 tiled.jpg图片