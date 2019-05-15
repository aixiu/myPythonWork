#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个类似秒表的程序

import time

# 给用户一个提示
print('按 Enter 键开始. 之后再按 Enter 键开始记录秒表时间。'
      '按下 Ctrl-C(Windows) command-F2(Mac) 退出秒表记时。')

input()
print('{:*^20}'.format('开始记录'))

startTime = time.time()   # 记录最开始的时间
lastTime = startTime
lapNum = 1    # 记数器，记录秒表按的次数

try:
    while True:
        input()
        lapTime = round(time.time() - lastTime, 2)  # 本次到上一次时间
        totalTime = round(time.time() - startTime, 2)   # 本次到开始的时间
        print('Lap #{}: {} ({})'.format(lapNum, totalTime, lapTime), end='')
        lapNum += 1
        lastTime = time.time()   # 记录上一次时间
except KeyboardInterrupt:    # 异常处理 
    print('\n{:*^20}'.format('记录完毕'))