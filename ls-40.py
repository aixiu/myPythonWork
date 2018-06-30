#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, subprocess   # 引用外部程序模块  subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

print('Music, Now!')

try:
    subprocess.run(['start', 'f4 - 流星雨.mp3'])   # 用subprocess 打开外部程序
except FileNotFoundError: 
    print('\n{:*^20}'.format('找不到播放文件'))

