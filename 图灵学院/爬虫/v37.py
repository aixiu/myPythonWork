#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入 chrome://version/ 查看chrome 版本信息！~

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
# chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("window-size=1024,768")
chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = r"D:\\Program Files\\Chrome\\Chrome\\chrome.exe"

# 添加浏览器实例，手动添加路径
dirver = webdriver.Chrome(executable_path=r"D:\\Program Files\\Python3\\Venvs\\chromedriver.exe", chrome_options=chrome_options)

url = 'http://www.baidu.com'

dirver.get(url)

text = dirver.find_element_by_id('wrapper').text

print(text)

