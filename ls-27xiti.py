#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2

with open('basicWithCover.pdf', 'rb') as pdfBasicFile:   # 打开文件，并建立对像
    pdfBasicFile = PyPDF2.PdfFileReader(pdfBasicFile)  # 读取全部内容并建立写入对象
    pdfWriter = PyPDF2.PdfFileWriter()   # 建立写对象

    for pagNum in range(1,pdfBasicFile.numPages):
        pageObj = pdfBasicFile.getPage(pagNum)  # 读取第2页至最后一页
        pdfWriter.addPage(pageObj)   # 用写入对象进行追加

    with open('basic.pdf', 'wb') as pdfOutputFile:  # 打开文件，添加 pdfOutputFile 对象
        pdfWriter.write(pdfOutputFile)     # 用写入对象把文件内写入新文件 basic.pdf

