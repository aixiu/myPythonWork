#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
使用代理访问百度网站
'''

from urllib import request, error

if __name__ == '__main__':

    url = 'https://www.baidu.com'

    # 1、设置代理地址
    proxy = {'http':'122.13.248.215:8888'}
    # 2、创建ProxyHandler
    proxy_handler = request.ProxyHandler(proxy)
    # 3、创建Opener
    opener = request.build_opener(proxy_handler)
    # 4、安装Opener
    request.install_opener(opener)

    # 现在如果访问 URL，则使用代理服务器
    try:
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0')
        
        rsp = request.urlopen(req)
        html = rsp.read().decode()

        print(html)

    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)