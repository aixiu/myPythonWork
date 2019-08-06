# 动态HTML

## 爬虫跟反爬虫

## 动态HTML介绍
- JavaScrapt
- jQuery
- Ajax
- python 采集动态数据
  - 从 javascript 代码入手采集
  - python 第三方库运行 javascript, 直接采集你在浏览器看到的页面

## Selenium + PhantomJS

### Selenium：web 自动化测试工具

- 自动加载页面
- 获取数据
- 截屏
- 安装：pip install selenium   带版本的  pip install selenium==2.48.0
- 官网：官网: http://selenium-python.readthedocs.io/index.html

- PhantomJS(幽灵浏览器)
  - 基于webkit 的无界面的浏览器
  - 官网：https://phantomjs.org/download.html
- Selenium 库有一个WebDrivers的API
- WEBDrivers 可以跟页面上的元素进行各种交互，用它可以来进行爬取
- 案例 v36

### chrome + chromedriver

- 下载安装 chrome   输入 chrome://version/ 查看chrome 版本信息！~
- 下载安装 chromedriver:  https://sites.google.com/a/chromium.org/chromedriver/home  下载与 chrome 对应的版本，
- Selenium 操作主要分两大类
  - 得到UI元素
    - find_element_by_id
    - find_elements_by_name
    - find_elements_by_xpath
    - find_elements_by_link_text
    - find_elements_by_partial_link_text
    - find_elements_by_tag_name
    - find_elements_by_class_name
    - find_elements_by_css_selector
  - 基于UI元素操作的模拟
    - 单击
    - 右建
    - 拖拽
    - 输入
    - 可以通过导入 ActionsChains 类来做到
- 参数设置：https://www.jianshu.com/p/8ec70859ae03
- 案例37