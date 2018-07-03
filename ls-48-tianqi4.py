#!/usr/bin/env python
# -*- coding: utf-8 -*-

#天气预报
#如未安装requests包请用：windows+r cmd 打开命令  输入pip install requests 回车
#api.map.baidu.com(百度服务器地址)
import json
import requests

AK = 'QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT'   # Obtain your from : api.map.baidu.com

def url_name(city_name):
    api = 'http://api.map.baidu.com/telematics/v3/weather?location='
    # api例子  'http://api.map.baidu.com/telematics/v3/weather?location=城市名字&output=json&ak=QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT'
    full_url = api + city_name + '&output=json' + '&ak=' + AK
    return full_url
    

while True:
    print('{:=^40}'.format('欢迎进入天气查询系统'))
    city = input('请输入您要查询的城市名称(按0退出)：')
    url = url_name(city)
    # print(url)
    requests = requests.get(url)
    if city == '0':
        print('您已退出天气查询系统！')
        break
    else:
        pass