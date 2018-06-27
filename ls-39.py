#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 日期模块
import datetime
import time

# 例一
# 把 unix 时间元年转换成 datetime 转换
# print(time.time())
# print(datetime.datetime.fromtimestamp(time.time()))
# print(datetime.datetime.fromtimestamp(10000000))

# 例二
# dn = datetime.datetime.now()
# # return 一个 datetim 对象
# print(dn)
# print('year:{}, month:{}, day:{},'
#       'hour:{}, minute:{}, second:{}'.format(dn.year, dn.month,
#        dn.day, dn.hour, dn.minute, dn.second))

# 例三
# dt = datetime.datetime(2017, 12, 20, 19, 16, 0)   # 用指定日期时间创建datetime
# print('year:{}, month:{}, day:{},'
#       'hour:{}, minute:{}, second:{}'.format(dt.year, dt.month,
#        dt.day, dt.hour, dt.minute, dt.second))

# 例四
# # datetime 的对象可以比较。后边的时间比前边的大
# springFestival = datetime.datetime(2018, 2, 16, 0, 0, 0)
# chrismas = datetime.datetime(2017, 12, 25, 0, 0, 0)
# dec252017 = datetime.datetime(2017, 12, 25, 0, 0, 0)

# print(chrismas != dec252017)
# print(springFestival > chrismas)

# 例五
# # timedelta 代表一个持续时间（时间段）
# delta = datetime.timedelta(weeks=1, days=11, hours=10, minutes=9, seconds=8)
# # 通过上述方法产生一个时间段对象

# print(delta.days, delta.seconds, delta.microseconds)
# print(delta.total_seconds())
# print(str(delta)) # 用 str(), 返回一个适合人们阅读的对象

# 例六
# dt = datetime.datetime.now()   # 当前时间
# thousandDays = datetime.timedelta(days=1000)   # 时间持时间1000天
# print(dt + thousandDays)   # 1000天以后的日期
# print(dt - thousandDays)   # 1000天以前的日期

# 例七
# newYear2019 = datetime.datetime(2019, 1, 1)  # 用指定日期时间创建datetime
# while datetime.datetime.now() < newYear2019:
#     time.sleep(1)

# 例八 strftime() 可以指定输出的日期格式
oct21st = datetime.datetime(2017, 10, 21, 16, 29, 0)
print(oct21st.strftime('%Y-%m-%d %H:%M:%S'))
print(oct21st.strftime('%I:%M %p'))
print(oct21st.strftime('%B of %Y'))


print(datetime.datetime.strptime('October 21 2015', '%B %d %Y'))
print(datetime.datetime.strptime('2015/10/21 16:29:00', '%Y/%m/%d %H:%M:%S'))
print(datetime.datetime.strptime('October of 15', '%B of %y'))
print(datetime.datetime.strptime('November of 63', '%B of %y'))
