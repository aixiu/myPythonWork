#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
利用parse 模块模拟 post请求
分析百度词典
分析步骤：
1、打开F12
2、尝试输入单词 girl,发现每敲一个字母后边都有请求
3、请求地址是 http://fanyi.baidu.com/sug
4、利用  NetWork-All-Hearders 查看 发现 FormDate的值是 kw:girl
5、检查返回内容格式，发现返回的是json格式内容，需要用到json包
'''

import requests
# 负责处理json格式的模块
from urllib import parse
import json
'''
大致流程是：
1、利用 data 构造内容，然后urlopen打开
2、返回一个json格式的结果
3、结果就应该是girl的释交
'''

baseurl = 'https://fanyi.baidu.com/sug'

# 存放用来模拟 form的数据，一定是 dict 格式
data = {'kw':'boy'}   # 查询数据 girl 写成硬编码

# 构建一个请求头，至少包含传入的数据的长度。
# request 要求传入的请求头是一个 dict 格式

headers = {
    # 因为使用 post ，至少包含 content-length 字段
    'Content-Length':str(len(data))
}


# 有了 headers,data, url 就可以尝试发出请求了
rsp = requests.post(baseurl, data=data, headers=headers)

print(rsp.text)
print(rsp.json)

# for item in json_data['data']:
#     print(item['k'], '--', item['v'])


