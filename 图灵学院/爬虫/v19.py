#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
破解有道词典
V2
用到的JS，为：fanyi.min.js
'''


'''
通过查找，能找到js代码中操作代码
1、这个是计算salt的公式  r = "" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
2、sign: n.md5("fanyideskweb" + e + r + "n%A-rKaT5fb[Gy?;N5@Tj")
md5,一共需要四个参数，第一个和第四个都是固定值字符串，第三个是所谓的salt ,
第二个参数就是输入的要查找的单词

https://blog.csdn.net/xiongzaiabc/article/details/80711899
'''


def getSalt():
    '''
    salt公式是："" + (new Date).getTime() + parseInt(10 * Math.random(), 10);
    把他翻译成python代码
    '''
    import time, random

    salt = int(time.time()*100) + random.randint(0, 10)
    return salt

def getMD5(v):
    import hashlib

    md5 = hashlib.md5()

    # update需要一个bytes格式参数
    md5.update(v.encode('utf-8'))  #要对哪个字符串进行加密，就放这里

    sign = md5.hexdigest() #拿到加密字符串

    return sign

def getSign(key, salt):

    sign = 'fanyideskweb' + key + str(salt) + 'n%A-rKaT5fb[Gy?;N5@Tj'

    sign = getMD5(sign)

    return sign


from urllib import request, parse

def youdao(key):

    url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'

    salt = getSalt()

    data = {
        'i': key,
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': str(salt),
        'sign': getSign(key, salt),
        'ts': '1564818487046',
        'bv': 'f7b23a95b2d4e9f5beafd6cf8d1ebaf0',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION'
    }

    # print(data)

    # 参数data 需要是bytes格式
    data = parse.urlencode(data).encode()

    headers = {
        'Accept': 'application/json, text/javascript, */*; q=0.01',
        # 'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,ru;q=0.7',
        'Connection': 'keep-alive',
        'Content-Length': len(data),
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
    youdao('boy')

    