#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
URLError的使用
'''

from urllib import request, error

if __name__ == '__main__':
    
    url = 'http://www.baiiiiidu.com'

    try:

        req = request.Request(url)
        rsp = request.urlopen(req)

        html = rsp.read().decode()
        print(html)

    except error.URLError as e:
        print('URLError: {}'.format(e.reason))
        print('URLError: {}'.format(e))
    except Exception as e:
        print(e)