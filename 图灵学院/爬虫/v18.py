#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
破解有道词典
V1
'''

from urllib import request, parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    data = {
        'i': 'girl',
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15648184870463',
        'sign': 'eac35384d87b922b7e89f7e6a701f494',
        'ts': '1564818487046',
        'bv': 'f7b23a95b2d4e9f5beafd6cf8d1ebaf0',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }

    # 参数data 需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': '241',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': 'OUTFOX_SEARCH_USER_ID=1643298505@10.169.0.84; JSESSIONID=aaaoaCaisSjfwbsaTCwXw; OUTFOX_SEARCH_USER_ID_NCOO=1448750892.8630915; ___rl__test__cookies=1564818487044',
        'Host': 'fanyi.youdao.com',
        'Origin': 'http://fanyi.youdao.com',
        'Referer': 'http://fanyi.youdao.com/',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.87 Safari/537.36',
        'X-Requested-With': 'XMLHttpRequest'
    }

    req = request.Request(url=url, data=data, headers=headers)

    rsp = request.urlopen(req)

    html = rsp.read().decode()

    print(html)

if __name__ == "__main__":
    youdao('girl')