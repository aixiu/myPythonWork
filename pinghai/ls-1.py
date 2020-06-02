#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 爬虫练习
    # 分析页面
        # URL = https://pinghailinfeng.gitee.io/archives/
        # 选择器知识
        # 定位URL路径

    # 用到的 python 模块
        # 标准模块 urllib
        # 自定义模块
        # 第三方库
            # requests 库

# 简单 DOM1

import requests
from lxml import etree
import cssselect
# 请求RUL地址
r = requests.get('https://pinghailinfeng.gitee.io/archives/')

# 请求响应  200 404 500  分别为，正常，资源不存在， 服务器异常
print(r.status_code)
print(r.headers)
print(r.encoding)


# 获取文本内容
print(r.text)

# 通过lxml 将网页将换成XML格式的数据
root = etree.HTML(r.text)
print(root)

#  通过CSSSELECT 或者 XPATH 语法，获取的都是列表
# 可以按列表操作取得元素
url = root.cssselect('#posts > article:nth-child(5) > header > h2 > a')
# attrib 属性 获取的是一个字典类型
print(url[0].attrib)

# 字典取值 根据 K, V操作

print(url[0].get('href'))


