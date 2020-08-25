#!/usr/bin/env python
# -*- coding: utf-8 -*-

#以parse模拟POST请求，大致流程：

# 1、利用data参数构造内容（关键字内容Form data）
# 2、使用urlopen()打开
# 3、返回的是JSON数据类型，使用json.loads()转换成字符串类型
# 4、结果就是搜索词girl的释义

from urllib import request, parse, error
# 处理近回数据 JSON
import json

# 建立基本 url
# 注意，将 https 换成 https

baseUrl = 'https://fanyi.baidu.com/sug'

# 防止报错，使用 error.URLerror

try:
    # 使用data参数构造内容，用以存放Form data
    # 提示用户输入关键字内容
    kw = input('Input your kw: ')

    # 使用data存放Form data，Request传入的必须是字典类型
    # 通过浏览器F12查看 ，发现form data下字典的key为kw，所以data的key为kw
    data = {
        'kw': kw
    }
    
    # 发送请求的URL为URL bybes类型，所以使用urlencode()转码
    # 服务器接收字节类型数据，所以要将关键字参数转换
    data = parse.urlencode(data).encode()
    print("即将发送的data数据的类型：{0}".format(type(data)))

    # 打开网页，传入data参数
    rsp = request.urlopen(baseUrl, data=data)

    # 读取内容，返回的内容为 tybes 类型，需转换为 str
    json_data = rsp.read().decode()
    print("查看返回数据的类型：{0}".format(type(json_data)))

    # 通过查看F12，返回的数据为json格式，所以转换
    json_data = json.loads(json_data)
    print("转换后的数据类型：{0}".format(type(json_data)))
    # print(json_data)

    # 因为是字典类型，所以可以使用for循环打印
    for i in json_data['data']:
        print(i)

except error.URLError as e:
    print(e)