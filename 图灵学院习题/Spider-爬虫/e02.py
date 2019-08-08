#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
构建代理集群/队列
每次访问服务器，随机抽取一个代理
抽取可以使用 random.choice

分析步骤：
1. 构建代理群
2. 每次访问，随机选取代理并执行
'''

from urllib import request, error

# 使用代理步骤
# 1. 设置代理地址
proxy_list = [
    # 列表中存放的是 dict类型的元素
    {"http": "117.191.11.102:80"},
    {"http": "117.191.11.74:80"},
    {"http": "117.191.11.110:8080"},
    {"http": "117.191.11.104:80"}
]


# 2、创建ProxyHandler
proxy_handler_list = []
for proxy in proxy_list: 
    proxy_handler = request.ProxyHandler(proxy)   # Proxyhandler代理处理器
    proxy_handler_list.append(proxy_handler)

# 3、创建Opener
opener_list = []
for proxy_handler in proxy_handler_list:
    opener = request.build_opener(proxy_handler)
    opener_list.append(opener)
    

import random

url = 'http://www.baidu.com'
# 现在如果访问url，则使用代理服务器
try:
    # 4. 安装Opener
    # choice() 方法返回一个列表，元组或字符串的随机项。
    opener = random.choice(opener_list)
    request.install_opener( opener)

    rsp = request.urlopen(url)
    html = rsp.read().decode()
    print(html)
except error.URLError as e:
    print(e)
except Exception as e:
    print(e)
