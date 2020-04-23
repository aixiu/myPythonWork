#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests

url = 'https://codemart.com/api/project?'

headers = {
    'accept':'application/json',
    'cookie':'_ga=GA1.2.1681064354.1587646281; _gid=GA1.2.2076573333.1587646281; mid=5d8baff9-e8c8-4c5b-8f0f-53abe8693f9a; JSESSIONID=7iu1yxpaudgvz2711bl8xgw0; _gat_gtag_UA_151094431_1=1; _gat=1',
    'referer':'https://codemart.com/projects',
    'user-agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'
}

response = requests.get(url, headers=headers).json()

data = response['rewards']

for i in data:
    name = i['name']
    roles = i['roles']