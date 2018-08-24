#!/usr/bin/env python
# -*- coding: utf-8 -*-

# PDF文件合并实例
import PyPDF2   # 导入PDF操作模块

# 打开二进制文件book.pdf,读取用'rb' 存入变量 pdfFlie中
pdfFlie = open('book.pdf', 'rb')  
# 用PyPDF2 把读取到的全部内容存入pdfReader中
pdfReader = PyPDF2.PdfFileReader(pdfFlie)
# 提取读取到的第一页 并存入 minutesFirstPage 变量中
minutesFirstPage = pdfReader.getPage(0)

# 打开二进制文件shuiyin.pdf,读取用'rb' 存入变量 markFile中
markFile = open('shuiyin.pdf', 'rb')
pdfWatermarkReader = PyPDF2.PdfFileReader(markFile)  # 读取其中全部内容

# 把‘book.pdf第一页和shuiyin.pdf第一样进行合并，完成添加水印’
minutesFirstPage.mergePage(pdfWatermarkReader.getPage(0))

pdfWriter = PyPDF2.PdfFileWriter()   # 写文件操作存入变量pdfWriter中
pdfWriter.addPage(minutesFirstPage)  # 先写入加好水印的第一页

for pageNum in range(1, pdfReader.numPages):   # 用for循环读取book.pdf第二页至最后一页
    pageObj = pdfReader.getPage(pageNum)     # 把读取到的内容写入pageObj变量
    pdfWriter.addPage(pageObj)               # 把内容添加到加好水印页的后边

# 因二进制文件不能直接在原文件改动只能新建一个文件，写的方式用'wb' 存入变量 resultPdfFile
# 文件 waterCover.pdf 如不存在直接生成
resultPdfFile = open('waterCover.pdf','wb')
pdfWriter.write(resultPdfFile)   # 把合并好的内容写入新文件

# 关闭所有已打开的文件
pdfFlie.close()
markFile.close()
resultPdfFile.close()