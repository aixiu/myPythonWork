#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

root_url = 'http://www.60addons.com'
url = 'http://www.60addons.com/bbs/topic/module/42-1'

headers = {
    'accept':'application/json',
    'cookie':'_ga=GA1.2.1681064354.1587646281; _gid=GA1.2.2076573333.1587646281; mid=5d8baff9-e8c8-4c5b-8f0f-53abe8693f9a; JSESSIONID=7iu1yxpaudgvz2711bl8xgw0; _gat_gtag_UA_151094431_1=1; _gat=1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

response = requests.get(url, headers=headers).text
# print(response)

# 提取诗歌连接
# 规则， 要求，取舍

poetry_urls = re.findall(r'<a class="tiezi" href="(.*)">.*</a>', response)

# print(poetry_urls)

# 获取数据`
for url in poetry_urls:
    poetry_html = requests.get(root_url + url).text
    # print(poetry_html)

#     # 正则（）提取数据
    poetry_infos_A = re.findall(r'<h3>(.*)</h3>', poetry_html)
    poetry_infos_B = re.findall(r'><p><a href=".*" rel="nofollow">.*</a> 密码:.*<br></p>', poetry_html)
#     for i in poetry_infos_A:
#         print(i)
    print(poetry_infos_A, poetry_infos_B)