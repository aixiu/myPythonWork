#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
URLError的使用
'''

from urllib import request, error

if __name__ == '__main__':
    
    url = 'http://v.hyage.com/aaa.html'

    try:

        req = request.Request(url)
        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print(html)

    except error.HTTPError as e:
        print('HTTPError: {}'.format(e.reason))
        print('HTTPError: {}'.format(e))

    except Exception as e:
        print(e)