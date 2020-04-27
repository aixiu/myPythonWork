#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ClassicWoW【官方怀旧】插件交流
# by辛迪加-萌新-猎人 QQ:332007851

import requests
from lxml import etree

url = 'http://www.60addons.com/bbs/topic/1908-1'

r = requests.get(url)

htmls = etree.HTML(r.text)

title = htmls.xpath("//h3//text()")[0]
change_log = htmls.xpath("//div[@class='panel-body']//p//text()")[10:14]

download_url = htmls.xpath("//div[@class='panel-body']//p//text()")[16]

download_password = htmls.xpath("//div[@class='panel-body']//p//text()")[17].split(':')[1]

print(title)
print(change_log)
print(download_url)
print(download_password)