#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 批量给图片加水印，注意是多张批量加
from pathlib import Path
from PIL import Image

PATH = 'E:/My_python_work/toAddLogo'   # 定义文件夹路径
LOGOFILENAME = 'liangzi.png'   # 定义水印图片

# 定义处理大水印图片的函数
# def resizlogo(p):
#     originalLogoIm = Image.open(str(p))  # open() 需是一个字符串所以用str
#     w, h = originalLogoIm.size

#     nWidth, nHeight = int(w/3), int(h/3)

#     nFilename = str(p.parent/'withLogo'/'smallLogo.png')  # 方法一  路径
#     # nFilename = Path.joinpath(withLogo/smallLogo.png)   # 方法二 路径
#     # 生成一缩小水印文件对象，并保存在 path路径下的，withLogo目录下，名字叫samllLogo.png
#     originalLogoIm.resize((nWidth, nHeight)).save(nFilename)  
#     # 把缩小版水印文件对象保存为文件
    
#     return nWidth, nHeight, nFilename

    

imagePath = Path(PATH)   # 建立路径对象

# 建立加好水印存放图片的文件夹
imageWithLogoFolder = imagePath.joinpath('withLogo')  # 建立一个withlogo 文件夹对象
imageWithLogoFolder.mkdir(777, exist_ok=True,)
# 生成 withlogo 文件夹 权限777 exist_ok=True --- 如果之前有这个文件夹会报错，加上exist_ok=True就不会报错。

# 如果水印 logo 尺寸太大，用定义的函数更改，并返回更改后的 长度，宽度，位置
# logowidth, logoHeight, logo = resizlogo(imagePath/LOGOFILENAME)
# (imagePath/LOGOFILENAME) 就是水印图片的地址
# logowidth, logoHeight, logo = resizlogo(imagePath.joinpath(LOGOFILENAME))  # 方法二

# logoIm = Image.open('logo')   # 如果是缩小过的用此地址
logoIm = Image.open('E:/My_python_work/toAddLogo/liangzi.png')
logoWidth, logoHeight = logoIm.size

# 开始添加水印
for fname in [x for x in imagePath.iterdir()]:
    # .iterdir() 返回一个迭代器, 包含path下所有文件/目录
    filename = fname.name   # 文件包含：文件名+扩展名   fname.name  就是取的文件名不含扩展名
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGOFILENAME:
        continue   # 判断文件是不是以png或jpg或是文件名为 LOGOFILENAME = 'liangzi.png' 就跳过本次循环
    
    imageLocation = imagePath.joinpath(filename)   # 新建对象 包含该文件的路径和文件名
    im = Image.open(imageLocation)   # 打开该文件 并放到im对象
    Width, Height = im.size    

    print('Adding logo to {}...'.format(filename))

    im.paste(logoIm, (Width - logoWidth - 30, Height - logoHeight - 30), logoIm)

    im.save(str(imagePath.joinpath('withLogo').joinpath(filename)))

# path(logo).unlink()   # 删掉上边把大水印缩小后的小LOGO文件