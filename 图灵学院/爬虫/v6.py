#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
任务要求和内容跟V5一样
本案例哈哈是利用 Request来实现V5的内容。

利用parse 模块模拟 post请求
分析百度词典
分析步骤：
1、打开F12
2、尝试输入单词 girl,发现每敲一个字母后边都有请求
3、请求地址是 http://fanyi.baidu.com/sug
4、利用  NetWork-All-Hearders 查看 发现 FormDate的值是 kw:girl
5、检查返回内容格式，发现返回的是json格式内容，需要用到json包
'''

from urllib import request, parse
# 负责处理json格式的模块
import json
'''
大致流程是：
1、利用 data 构造内容，然后urlopen打开
2、返回一个json格式的结果
3、结果就应该是girl的释交
'''

baseurl = 'http://fanyi.baidu.com/sug'

# 存放用来模拟 form的数据，一定是 dict 格式
data = {'kw':'girl'}   # 查询数据 girl 写成硬编码

# 需要使用parse 模块对 data 进行编码
data = parse.urlencode(data).encode('utf-8')

# 构建一个请求头，至少包含传入的数据的长度。
# request 要求传入的请求头是一个 dict 格式

headers = {
    # 因为使用 post ，至少包含 content-length 字段
    'Content-Length':len(data),
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36",
}
# 构造一个 Request的实例
req = request.Request(baseurl, headers=headers)

# 因为已经构造了一个Request,的请求实例，则所有的请求信息都可以封装在Request 实例中。
rsp = request.urlopen(req, data=data)

json_data = rsp.read().decode('utf-8')
print(type(json_data))
print(json_data)

# 把json字符串转化成字典
json_data = json.loads(json_data)
print(type(json_data))
print(json_data)


for item in json_data['data']:
    print(item['K'], '--', item['v'])


