#!/usr/bin/env python
# -*- coding: utf-8 -*-

from datetime import datetime

# 获取当前时间
now = datetime.now()  # 获取当前datetime
print(now)

# 获取指定时间
dt = datetime(2018, 8, 24, 19, 35, 20) # 用指定日期时间创建datetime
print(dt)


# 知识点：

# 你可以认为：
# timestamp = 0 = 1970-1-1 00:00:00 UTC+0:00

# 对应的北京时间是：
# timestamp = 0 = 1970-1-1 08:00:00 UTC+8:00


# datetime 转换为  timestamp
# 把一个datetime类型转换为timestamp只需要简单调用timestamp()方法：

print(dt.timestamp())  # 把datetime转换为timestamp

# timestamp 转换为 datetime
# 要把timestamp转换为datetime，使用datetime提供的fromtimestamp()方法：

t = 1535110520.0
print(datetime.fromtimestamp(t))  # 本地时间

print(datetime.utcfromtimestamp(t))  # UTC时间


# str转换为datetime
# 很多时候，用户输入的日期和时间是字符串，要处理日期和时间，首先必须把str转换为datetime。
# 转换方法是通过datetime.strptime()实现，需要一个日期和时间的格式化字符串：

cday = datetime.strptime('2019-6-1 18:24:55', '%Y-%m-%d %H:%M:%S')
print(cday)

# datetime转换为str
# 如果已经有了datetime对象，要把它格式化为字符串显示给用户，就需要转换为str，
# 转换方法是通过strftime()实现的，同样需要一个日期和时间的格式化字符串：

now = datetime.now()
print(now.strftime('%a, %b %d %H:%M'))