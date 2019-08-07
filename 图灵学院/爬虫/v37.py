#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 输入 chrome://version/ 查看chrome 版本信息！~

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

chrome_options = Options()
chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument("--no-sandbox")
chrome_options.binary_location = r"D:\\Program Files\\Chrome\\Chrome\\chrome.exe"

# 添加浏览器实例，手动添加路径
dirver = webdriver.Chrome(executable_path=r"D:\\Program Files\\Python3\\Venvs\\chromedriver.exe", chrome_options=chrome_options)

url = 'http://www.baidu.com'

dirver.get(url)

text = dirver.find_element_by_id('wrapper').text
print(text)

print(dirver.title)

# 获取页面的快照
dirver.save_screenshot('index.png')

# id='kw'的，是百度的输入框，得到输入框的UI元素后直接输入‘大熊猫’  .send_keys（）是输入的意思
dirver.find_element_by_id('kw').send_keys(u'大熊猫')

# 点击查找按钮  # id='su' 是百度搜索的按钮， click模拟点击

dirver.find_element_by_id('su').click()

time.sleep(5)
dirver.save_screenshot('daxiongma.png')


# 获取当前页面的cookie
print(dirver.get_cookies())


# 模拟输入两个按键 ctrl+a 
dirver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')

# ctrl+x 是剪切键
dirver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'x')

dirver.find_element_by_id('kw').send_keys(u'航空母舰')
dirver.save_screenshot('hangmu.png')

# 点击查找按钮  # id='su' 是百度搜索的按钮， click模拟点击

dirver.find_element_by_id('su').send_keys(Keys.RETURN)
time.sleep(5)
dirver.save_screenshot('hangmu2.png')

# 清空输入框
dirver.find_element_by_id('kw').clear()
dirver.save_screenshot('clear.png')

# 关闭浏览器
dirver.quit()