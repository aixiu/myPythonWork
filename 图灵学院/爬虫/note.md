# 准备工作

## 参资料

- python网络数据采集，图灵工业出版
- 精通python爬虫框架 Scrapy, 人民邮电出版社
- [Python3网络爬虫](http://blog.csdn.net/c406495762/article/details/72858983)
- [Scrapy宜方教程](http://scrapy-chs.readthedocs.io/zh_CN/0.24/intro/tutorial.html)

## 前提知识

- url
- http协议
- web前端，html, css, js
- ajax
- re, xpath
- xml

## 1、爬虫简介

- 爬虫定义 :网络爬虫 (又被称为网页蜘蛛，网络机器人 ，在F0AF社区 中间，更经常的称为网 页追逐者)，是一种按照一定的规则，自动地抓取万维网信息的程序或者脚本。另外一些不常使用的名字还有蚂蚁、自动索引、模拟程序或者蠕虫。

- 两大特征
  - 能按作者要求下载数据或者内容
  - 能自动在网络上流窜

- 三大步骤
  - 下载网页
  - 提取正确的信息
  - 根据一定规则自动跳到另外的网页上执行上两步内容

- 爬虫分类
  - 通用爬虫
  - 专用爬虫（聚焦爬虫）

- python网络包简介
  - python2.x: urllib, urllib2, urllib3, httplib, httplib2, requests
  - python3.x: urllib, urllib3, httplib2, requestts
  - python2: urllib 和 urllib2 配合使用，或者 requests
  - python3: urllib, requests

## 2、urllib

- 包含模块
  - urllib.request: 打开和读取 urls
  - urllib.error: 包含urllib.request产生的常见错误， 使用 try 捕捉
  - urllib.parse: 包含解析 url的方法
  - urllib.robotparse: 解析 robots.txt 文件
  - 案例V1

- 网页编码问题解决
  - chardet 可以自动检测页面文件的编码格式，但是，可能有误
  - 需要安装， 安装方法： pip install chardet
  - 案例V2
  
- urlopen 的返回对象
  - 案例V3
  - geturl:返回请求对象的 url
  - info:请求反馈对象的meta信息
  - getcode:返回http code 如： 1XX， 200， 404， 等

- request.date 的使用
  - 访问网络的两种方法
    - get:
      - 利用参数给服务器传递信息
      - 参数为 dict ，然后用 parse 编码
      - 案例V4
    - post
      - 一般向服务器传递参数使用
      - post是信息自动加密处理
      - 如果想使用 post 信息，需要用到 data 参数
      - 使用 post 意味着http的请求头可能需要更改：
        - Content-Type: application/x-www.form-urlencode
        - Content-Length: 数据长度
        - 简而言之，一旦更改请求方法，请注意其它请求头部信息相适应
      - urllib.parse.urlencode 可以将字符串自动转 成上面的
      - 案例V5
      - 为了更多的设置请求信息，单纯的通过urlopen函数已经不太好用了
      - 需要利用request.Request 类
      - 案例V6

- urllib.error
  - URLError产生的原因：
    - 没网
    - 服务器链接失败
    - 服务器问题
    - 是OSError的一个子类
    - 案例v7
  - HTTPError, 是 URLError的一个子类
    - 案例v8

  - HTTPError和URLError的两者区别
    - HTTPError 是对应的HTTP请流动的返回码错误， 如果返回错误码是400以上的，则引发HTTPError
    - URLError对应一般是网络出现问题，包括URL问题
    - 关系区别：OSError-URLError-HTTPError

- UserAgent
  - UserAgent: 用户代理，简秒UA， 属于heads 的一部分，服务器通过UA来判断访问者身份
  - 常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问访问的时候抓包

```html
常见的UA值，使用的时候可以直接复制粘贴，也可以用浏览器访问的时候抓包：
1.Android

Mozilla/5.0 (Linux; Android 4.1.1; Nexus 7 Build/JRO03D) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.166 Safari/535.19

Mozilla/5.0 (Linux; U; Android 4.0.4; en-gb; GT-I9300 Build/IMM76D) AppleWebKit/534.30 (KHTML, like Gecko) Version/4.0 Mobile Safari/534.30

Mozilla/5.0 (Linux; U; Android 2.2; en-gb; GT-P1000 Build/FROYO) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1

2.Firefox

Mozilla/5.0 (Windows NT 6.2; WOW64; rv:21.0) Gecko/20100101 Firefox/21.0

Mozilla/5.0 (Android; Mobile; rv:14.0) Gecko/14.0 Firefox/14.0

3.Google Chrome

Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/27.0.1453.94 Safari/537.36

Mozilla/5.0 (Linux; Android 4.0.4; Galaxy Nexus Build/IMM76B) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.133 Mobile Safari/535.19

4.iOS

Mozilla/5.0 (iPad; CPU OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A334 Safari/7534.48.3

Mozilla/5.0 (iPod; U; CPU like Mac OS X; en) AppleWebKit/420.1 (KHTML, like Gecko) Version/3.0 Mobile/3A101a Safari/419.3

链接：https://www.jianshu.com/p/844b4b674ee5
```

- 设置UA可以通过两种方式：
  - heads
  - add_header
  - 案例v9

- ProxyHandler 处理（代理服务器）
  - 使用代理IP，是爬虫的常用手段
  - 获取代理服务器的地址：
    - www.xicidaili.com
    - www.goubanjia.com
  - 代理用来隐藏真实访问中，代理也不允许频繁访问某一个固定网站，所以，代理一定要很多
  - 基本使用步骤：
    - 1、设置代理地址
    - 2、创建ProxyHandler
    - 3、创建Opener
    - 4、安装Opener
  -案例v10

- cookie & seesion
  - 由于http协议的无记忆性，人们为了弥补这个缺憾，采用一个补充协议
  - cookie是发放给用户（即http浏览器）的一段信息，session是保存在服务器上的对应的另一半信息，用来记录用户信息。
- cookie & seesion区别
  - 存放位置不同
  - cookie不安全
  - seeesion会保存在服务器上一定时间，会过期
  - 单个cookie 保存数据不超过4K，很多浏览器限制一个站点最多保存20个
- session的存放位置
  - 存在服务器端
  - 一般情况，session是放在内存中或者数据库中。
  - 没有cookie登录  案例v11, 可以看到，没有使用cookie 则反馈网页为未登录状态。

- 使用 cookie 登录
  - 直接把cookie 复制下来，然后手动放入请求头，案例 v12
  - http 模块包含一些关于 cookie 的模块，能过他们我们可以自动使用cookie

    - Cookiejar
      - 管理存储cookie, 向传出的 https 请求，添加 cookie
      - cookie，存储在内存中， Cookiejar 实例回收后  cookie将消失

    - FileCookiejar(filename, delayload=None, policy=None)：
      - 使用文件管理Cookie
      - filename是保存Cookie的文件

    - MozillaCookiejar(filename, delayload=None, policy=None)：
      - 创建与 mocilla 浏览器cookie.txt兼容的FileCookiejar 实例

    - LwpCookiejar(filename, delayload=None, policy=None)：
      - 创建与libwww-perl 标准兼容的 Set-Cookie3格式的 FileCookiejar 实例

    - 他们的关系是 Cookiejar --> FileCookiejar --> MozillaCookiejar & LwpCookiejar

  - 利用 Cookiejar 访问人人网，案例V13
    - 自动使用cookie登录，大致流程：
    - 打开登录页面后自动通过用户名密码登录
    - 自动提取反馈回来的cookie
    - 利用提取的cookie登录隐私页面

  - handler 是Handler的实例，常用的参看代码
    - 用来处理复杂请求

      ```txt
      # 生成 cookie的管理器
      cookie_handler = request.HTTPCookieProcessor(cookie)

      # 创建http请求管理器
      http_handler = request.HTTPHandler()

      # 创建https请求管理器
      https_handler = request.HTTPSHandler()
      ```

  - 创建handler后，使用opener打开，打开后相应的业务由相应的hanlder处理

    ```txt
    # .urlopen()函数不支持验证、cookie或者其它HTTP高级功能。要支持这些功能，必须使用build_opener()函数创建自定义Opener对象。
    opener = request.build_opener(http_handler, https_handler, cookie_handler)
    ```

  - cookie作为一个变量，打印出来，案例 v14
    - cookie的属性
      - name: 名称
      - value: 值
      - domain: 可以访问此cookie 的域名
      - path: 可以访问此cookie的页面路径
      - exires: 过期时间
      - size: 大小
      - Http字段

  - cooke的保存-FileCookiejar 案例v15
