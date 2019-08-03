#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
利用 request 下载页面
自动检测页面编码
'''

from urllib import request, parse

if __name__ == '__main__':
    
    url = 'http://www.baidu.com/s?'
    wd = input('请输入关键字：')
    
    # 要想使用 date ，需要使用字典结构
    qs= {'wd':wd}

    qs = parse.urlencode(qs)
    print(qs)

    fullurl = url + qs
    print(fullurl)

    rsp = request.urlopen(fullurl)

    html = rsp.read()
   

    # 使用 get 取值保证不会出错
    html = html.decode()

    print(html)