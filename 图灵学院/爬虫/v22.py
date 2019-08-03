#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
使用参数 headers 和 params
研究返回结果
'''

import requests

# 完整访问RUL是下面URL加上参数构成
url = 'http://www.baidu.com/s?'

kw = {
    'wd':'量子'
}

headers = {
    'User-Agnet':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36'
}
rsp = requests.get(url, params=kw, headers=headers)

print(rsp.text)
print(rsp.content)
print(rsp.url)
print(rsp.encoding)
print(rsp.status_code)  # 请求返回码