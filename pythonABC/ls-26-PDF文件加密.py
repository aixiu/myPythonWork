#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 对 PDF 文件进行加密
import PyPDF2

# 把 shuiyin.pdf 以二进制方式 读取到 pdfFile对象
with open('shuiyin.pdf', 'rb') as pdfFile:
    # 把 pdf 文件所有内容读取后存入 pdfReader 对象
    pdfReader = PyPDF2.PdfFileReader(pdfFile)
    #创建一个写对象 pdfWriter
    pdfWriter = PyPDF2.PdfFileWriter()

    for pageNum in range(pdfReader.numPages):   # 遍历读对象所有面页
        pdfWriter.addPage(pdfReader.getPage(pageNum)) # 把读对象拿到所有数据追加到写对象

    pdfWriter.encrypt('aixiu')  # 对写对象设置密码

    # 打开并创建文件 mishuiyin.pdf 存入 resuItPdf 对象
    with open('mishuiyin.pdf', 'wb') as resultPdf:
        pdfWriter.write(resultPdf)   # 将所有读对象的内容写入到写对象