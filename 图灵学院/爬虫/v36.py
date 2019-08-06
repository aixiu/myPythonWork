#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
通过webdriver操作百度进行查找
'''

from selenium import webdriver
import time

# 通过 Keys 模拟键盘
from selenium.webdriver.common.keys import Keys

# 操作哪个浏览器就对哪个浏览器建立一个实例
# 自动按照环境变量查找相应的浏览器
driver = webdriver.PhantomJS(executable_path=r'D:/Program Files/Python3/Venvs/phantomjs-2.1.1/bin/phantomjs.exe')

# 如果浏览器没有相应环境变量中，需要找定浏览器位置

# 获取指定网页的数据
driver.get('https://www.baidu.com')

# 通过函数查找 title 标签
print('Title:{}'.format(driver.title))

