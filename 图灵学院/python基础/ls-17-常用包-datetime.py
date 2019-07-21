#!/usr/bin/env python
# -*- coding: utf-8 -*-

# datetime 模块
    # datetime提供日期和时间的运算和表示

import datetime

# datetime常见属性
    # datetime.date: 一个理想和的日期，提供year, month, day属性

dt = datetime.date(2018, 3,26)
print(dt)
print(dt.day)
print(dt.year)
print(dt.month)

# datetime.time: 提供一个理想和的时间， 具于 hour， minute，sec，microsec等内容
# datetime.datetime: 提供日期跟时间的组合
# datetime.timedelta: 提供一个时间差，时间长度


# datetime.datetime
from datetime import datetime
# 常用类方法：
# today： 
# now
# utcnow
# fromtimestamp： 从时间戳中返回本地时间
dt = datetime(2019, 5, 26)
print(dt.today())
print(dt.now())