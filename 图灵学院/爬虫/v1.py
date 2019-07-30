#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request
'''
使用urllib.request 请求一个网岩浆内容，并把内容打印出来
本例使用 ：https://sou.zhaopin.com/?jl=530&kw=python&kt=3  地址，随便点一下进去
'''

if __name__ == '__main__':
    url = 'https://jobs.zhaopin.com/CC373968916J00153104409.htm'

    # 打开相应 URL 并把相应页面作为返回
    rsp = request.urlopen(url)

    # 把返回结果读取出来
    # 读取出来的内容类型为 bytes
    html = rsp.read()
    print(type(html))

    # 如果想把  byest 内容转换成字符串，需要解码
    html = html.decode('utf-8')
    print(html)