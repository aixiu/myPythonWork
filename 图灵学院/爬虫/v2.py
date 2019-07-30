#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
利用 request 下载页面
自动检测页面编码
'''

import urllib.request
import chardet

if __name__ == '__main__':
    
    url = 'http://finance.eastmoney.com/a/201907301192417876.html'

    rsp = urllib.request.urlopen(url)

    html = rsp.read()

    #利用 chardet 自动检测
    cs = chardet.detect(html)
    print(type(cs))
    print(cs)

    # 使用 get 取值保证不会出错
    html = html.decode(cs.get('encoding', 'utf-8'))
    # print(html)