#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.MozillaCookieJar()
cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建https请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
# .urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象。
opener = request.build_opener(http_handler, https_handler, cookie_handler)



def getHomPage():
    url = 'http://www.renren.com/882859385/profile'

    # 如果已经执行了login函数，则 opener自动已经包含相应的cookie值
    rsp = opener.open(url)

    html = rsp.read().decode()


    with open('rsp.html', 'w')  as f:
        f.write(html)

if __name__ == '__main__':

    getHomPage()