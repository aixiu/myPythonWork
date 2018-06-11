#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 随机函数创建一个列表，进行大小排序，此方法称为冒泡法。

import random

numlist = []
M = 10

for i in range(M):
    numlist.append(random.randrange(1,10))

print(numlist)

i = len(numlist) - 1

while i > 0:

    j = 0

    while j < i:
        if numlist[j] > numlist[j+1]:
            numlist[j],numlist[j+1] =  numlist[j+1],numlist[j]

        j += 1
    for k in numlist:
        print(k,end=",")
    print()

    i -= 1
