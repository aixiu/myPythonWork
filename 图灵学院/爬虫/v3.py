#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
利用 request 下载页面
自动检测页面编码
'''

import urllib.request

if __name__ == '__main__':
    
    url = 'http://finance.eastmoney.com/a/201907301192417876.html'

    rsp = urllib.request.urlopen(url)
    print(type(rsp))
    print(rsp)

    print('URL:{}'.format(rsp.geturl()))
    print('Info:{}'.format(rsp.info()))
    print('Code:{}'.format(rsp.getcode()))

    html = rsp.read()

   

    # 使用 get 取值保证不会出错
    html = html.decode()