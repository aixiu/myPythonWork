#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 常用模块
    # calendar
    # time
    # datetime
    # timeit
    # os
    # shutil
    # zip
    # math
    # string
    # 上述所有模块使用，得先导入，string是特例
    # calendar, time, datetime 的区别参考中文意思

# calendar
    # 跟日历相关的模块

import calendar

    # calendar：　获取一年的日历字符串
    # 参数
    # w = 每个日期之间的间隔字符数
    # l = 每周所占用的行数
    # c = 每个月之间的间隔字符数

cal = calendar.calendar(2019)
print(type(cal))

# cal = calendar.calendar(2019, l=0, c=5)

# isleap: 判断某一年是否闰年
calendar.isleap(2019)

# leapdays: 获取指定年份之间的闰年的个数
calendar.leapdays(2001, 2019)

help(calendar.leapdays)

# month（） 获取某个月的日历字符串
# 格式:calendar.month(年，月)
# 回值：月日历的字符串
m3 = calendar.month(2019, 3)
print(m3)


# monthrange（） 获取一个月的周几开始即和天数
# 格式：calendar.monthrange(年,月)
# 回值：元组(周几开始,总天数)
# 注意：周默认 0 -6 表示周一到周天

w, t = calendar.monthrange(2019, 3)
print(w)
print(t)



# monthcalendar() 返回一个月每天的矩阵列表
# 格式：calendar.monthcalendar(年，月)
# 回值：二级列表
# 注意：矩阵中没有天数用0表示
m = calendar.monthcalendar(2019, 3)
print(type(m))
print(m)


# prcal: 直接打印日历  print calendar

calendar.prcal(2019)


# prmonth() 直接打印整个月的日历
# 格式：calendar.prmonth(年，月)
# 返回值：无
calendar.prmonth(2019, 5)



# weekday() 获取周几
# 格式:calendar.weekday(年，月，日)
# 返回值:周几对应的数字
calendar.weekday(2019, 5, 25)