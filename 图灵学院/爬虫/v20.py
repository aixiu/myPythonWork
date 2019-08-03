#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
以参数的方试传递参数用 get方式
以 form方式传递参数用  post方式
爬取豆瓣电影数
了解ajax的基本爬取方式
分析URL地址：

https://movie.douban.com/j/chart/top_list?type=11&
interval_id=100%3A90&
action=&
start=40&
limit=20
'''
from urllib import request
import json

url = 'https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=20&limit=20'

rsp = request.urlopen(url)

data = rsp.read().decode()

# json.loads()解码成 python json格式
# json.load()加载 python json格式文件
# https://blog.csdn.net/qq_39198486/article/details/81608288
data = json.loads(data)

print(data)