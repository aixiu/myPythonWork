#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time, subprocess

timeLeft = 5
while timeLeft > 0:
    print(timeLeft)
    time.sleep(1)
    timeLeft -= 1

print('Music, Now!')

try:
    subprocess.run(['start', 'f4 - 流星雨.mp3'])
except FileNotFoundError: 
    print('\n{:*^20}'.format('找不到播放文件'))

