#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://www.baidu.com'

#  两种请求方式
# 方式一  使用 get 请求
rsp = requests.get(url)
print(rsp.text)


# 使用request 请求
rsp = requests.request('get', url)
print(rsp.text)
