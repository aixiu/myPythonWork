#!/usr/bin/env python
# -*- coding: utf-8 -*-

import PyPDF2

with open('book.pdf', 'rb') as pdfFileObj:
    pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

    numpages = pdfReader.numPages

    print('文件共有 {} 页'.format(numpages))

    pageObj =  pdfReader.getPage(0)
    print(pageObj.extractText())     # 打印PDF文件的内容