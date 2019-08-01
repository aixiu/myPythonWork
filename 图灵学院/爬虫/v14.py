#!/usr/bin/env python
# -*- coding: utf-8 -*-

#!/usr/bin/env python
# -*- coding: utf-8 -*-

from urllib import request, parse
from http import cookiejar

# 创建cookiejar的实例
cookie = cookiejar.CookieJar()

# 生成 cookie的管理器
cookie_handler = request.HTTPCookieProcessor(cookie)

# 创建http请求管理器
http_handler = request.HTTPHandler()

# 创建https请求管理器
https_handler = request.HTTPSHandler()

# 创建请求管理器
# .urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象。
opener = request.build_opener(http_handler, https_handler, cookie_handler)

# 登录函数，负责初次登录， 需要输入用户名和密码，用来获取登录cookie 凭证
def login():
    # 此URL需要从登录 form的 action 属性中提取（查看网页源码）
    url = 'http://www.renren.com/PLogin.do'

    # 此键值需要从登录form的两个对应的 imput 中提取 name属性（查看网页源码）
    data = {
        'email':'4815563@qq.com',
        'password':'shendlax520'
    }

    # 对据进行编码
    data = parse.urlencode(data)

    # 创建一个请求对象
    req = request.Request(url, data=data.encode())

    # 使用opener发起请求
    rsp = opener.open(req)


if __name__ == '__main__':
    ''''
    执行完loging后，会得到受权之后的cookie 
    尝式把cookie打印出来
    '''
    login()
    print(cookie)

    for item in cookie:
        print(type(item))
        print(item)

        # dir() 函数不带参数时，返回当前范围内的变量、方法和定义的类型列表；
        # 带参数时，返回参数的属性、方法列表。
        # 如果参数包含方法__dir__()，该方法将被调用。
        # 如果参数不包含__dir__()，该方法将最大限度地收集参数信息。
        for i in dir(iter):
            print(i)