#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
访问一个网址
更改自己的UserAgent进行伪装
'''

from urllib import request, error

if __name__ == '__main__':

    url = 'http://www.baidu.com'

    try:
        # 方法一
        # 使用headers方法伪装UA
        # headers = {}
        # headers['User-Agent'] = 'Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3'

        # req = request.Request(url, headers=headers)

        # 方法二
        # 使用add_header方法
        req = request.Request(url)
        req.add_header('User-Agent', 'Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0')

        # 正常记问
        rsp = request.urlopen(req)
        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print(e)
    except error.URLError as e:
        print(e)
    except Exception as e:
        print(e)
    
    print('DONE>..........')
