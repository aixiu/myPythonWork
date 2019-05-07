#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 编写一个程序，求 100~199 之间的所有水仙花数。
    # 如果一个3位数等于其各个位数的立方和，则称这个数为水仙花数。
    # 例如：153 = 1的3次方 + 5的3次方 + 3的3次方，因此 153 就是一个水仙花数。

for i in range(100, 1000):
    temp = str(i)
    a = int(temp[0])
    b = int(temp[1])
    c = int(temp[2])
    if a**3 + b**3 + c**3 == i:
        print(i)

