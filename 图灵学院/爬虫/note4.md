# scrapy

## 爬虫框架
  
- 框架
- 爬虫框
  - scrapy
  - pyspider
  - crawley
- scrapy框架介绍
  - https://doc.scrapy.org/en/latest/
  - http://scrapy-chs.readthedocs.io/zh_CN/latest/index.html

- 安装
  - 利用pip安装  pip install scrapy

- scrapy 概述
  - 包含各个部件
    - ScrapyEngine: 神经中枢，大脑，核心
    - Scheduler调度器：引擎发来的request请求，调度器需要处理，然后交换引擎
    - Downloader下载器：把引擎发来的 requests 发出请求，得到response
    - Spider爬虫：负责把下载器得到的网页/结果进行分解，分解成数据+链接
    - ItemPipeline 管道：详细处理Item
    - DownloaderMiddleware下载中间件：自定义下载的功能扩展组件
    - SpiderMiddleware爬虫中间件：对spider进行功能扩展

- 爬虫项目大概流程
  - 新建项目： scrapy startproject XXX
  - 明确需要目标/产出：编写item.py
  - 制作爬虫：地址 spider/xxspider.py
  - 存储内容：pipelines.py

- ItemPipeline 
  - 爬虫提取出据存入item后，item中保存的数据需要进一步处理，比如清洗，去重，存储等。
  - pipeline需要处理 process_item函数
    - process_item:
      - spider提取出来的item作为参数传入，同时传入的还有 spider
      - 此方法必须实现
      - 必须返回一个 Item对象，被丢弃的item不会被之后的pipeline处理
    - __init__:构造函数
      - 进行一些必要的参数初始化
    - open_spider(spider):
      - spider 对象被开时调用
    - close_spider(spider):
      - 当spider对象被关闭时调用

- Spider
  - 对应的是文件夹 spiders 下的文件
  - __init__: 初始化爬虫名称，star_urls列表
  - start_requests:生成 Requests对象交给 scrapy下载并返回 response
  - parse: 根据返回的response 解析出相应的 item, item自进入 pipeline; 如果需要，解析出 url, url自动交给 requests 模块，一直循环下去
  - start_requests:此方法仅能被调用一次，读取start_urls内容并动循环过程。
  - name： 设置爬虫名称
  - start_urls: 设置开始第一批爬取的url
  - allow_domains: spider允许爬取的域名列表
  - start_request(self): 只被调用一次
  - parse
  - log:日志记录
  
- 案例 e14-scrapy-baidu
  - 利用最简单的爬虫
  - 爬取百度面页
  - 关闭配置机器人协议
  - scrapy startproject baidu
  - scrapy crawl baidu

- 案例 e15-meiju
  - 创建新项目
  - 分析网页，定义 item
  - 编写 pipeline,确定如何处理 item
  - 编写 spider,确定如何提取item
  - 可以通过增加一个单独命令文件的方式在 pycharm 中启动爬虫