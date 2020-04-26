#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
import re

url = 'https://so.gushiwen.org/gushi/tangshi.aspx'
root_url = 'https://so.gushiwen.org'

headers = {
    'accept':'application/json',
    'cookie':'_ga=GA1.2.1681064354.1587646281; _gid=GA1.2.2076573333.1587646281; mid=5d8baff9-e8c8-4c5b-8f0f-53abe8693f9a; JSESSIONID=7iu1yxpaudgvz2711bl8xgw0; _gat_gtag_UA_151094431_1=1; _gat=1',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

response = requests.get(url, headers=headers).text
# print(response)

# 提取诗歌连接
# 规则， 要求，取舍

poetry_urls = re.findall(r'<span><a href="(.*)" target="_blank">.*</a>\(.*\)</span>', response)

# print(poetry_urls)

# 获取数据
for url in poetry_urls:
    poetry_html = requests.get(root_url + url).text
    # print(poetry_html)

    # 正则（）提取数据
    poetry_infos = re.findall(r'<textarea style=.*>(.*)——(.*)《(.*)》.*</textarea>', poetry_html)
    # print(poetry_infos)

    # 数据的调整
    for i in poetry_infos:
        poetry_content_A = i
        # print(poetry_content_A)

    poetry_content = '\n'.join((reversed(poetry_content_A)))
    print(poetry_content)

    with open('poetry.txt', 'a', encoding='utf-8') as f:
        f.write('{}{}'.format(poetry_content, '\n'))
