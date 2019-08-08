#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
爬取百度贴吧-张继科
1、 贴吧主页是 https://tieba.baidu.com/f?kw=张继科
2、进去之后，有很多页，
    第一页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=0
    第二页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=50
    第三页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=100
    第四页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=150
    第五页网址是：https://tieba.baidu.com/f?kw=张继科&ie=utf-8&pn=200
3、由上面网址可以找到规律，每一页只有后面数字不同，且数字应该是（页数-1）X50 

解决方法：
1. 准备构建参数字典
    字典包含三部分，kw，ie，pn
2. 使用parse构建完整url
3. 使用for循环下载
'''

from urllib import request, parse

if __name__ == '__main__':
    # 1、准备构建参数字典：
    qs= {'kw':'张继科', 'ie':'utf-8', 'pn':0}

    # 2、使用parser构建完整url
    # 假定只需要前10页
    urls = []
    baseurl = "https://tieba.baidu.com/f?"  # 基础的url

    for i in range(10):
        pn = i * 50
        qs['pn'] =  str(pn)

        # 把qs编码后和基础url进行拼接
        # 拼接完毕后装入url列表中
        urls.append(baseurl + parse.urlencode(qs))

    print(urls)

    for url in urls:
        rsp = request.urlopen(url)
        html = rsp.read().decode('utf-8')

        print(url)
        # print(html)