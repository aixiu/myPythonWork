#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 作业一
# 写一个程序，判断给定年份是否为闰年
    # 闰年的定义：能够被 4 整除的年份就是闰年

year = input('请输入年份===>')  # type: str

if year.isdigit(): # isdigit() 方法检测字符串是否只由数字组成。
    year = int(year)
    if year % 4 == 0:
        print('{} 是闰年'.format(year))
    else:
        print('{} 不是闰年'.format(year))
else:
    print('输入的是年份吗？')


# 作业二
# 给用户三次机会，猜想我们程序生成的一个数字 A，
# 每次用户猜想过后会提示数字是否正确以及用户输入数字是大于还是小于 A，
# 当机会用尽后提示用户已经输掉

import random

secert = random.randint(1, 10)  # 生成随机整数

times = 3  # 用户可猜的次数

while times:
    num = input('请输入数字：')   # type: str
    if num.isdigit():
        num = int(num)
        if num == secert:
            print('你猜对了')
            break
        elif num < secert:
            print('你猜的数字小了')
            times -= 1
        else:
            print('你猜的数字大了')
            times -= 1
    else:
        print('你输的不是数字！重来。')

print('游戏结束')

