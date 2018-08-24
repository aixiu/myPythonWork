#!/usr/bin/env python
# -*- coding: utf-8 -*-


data = [10, 4, 33, 21, 54, 3, 8, 11, 5, 22, 2, 1, 17, 13, 6]

for i in range(len(data)-1):
    for j in range(len(data)-1-i):
        if data[j] > data[j+1]:
            data[j], data[j+1] = data[j+1], data[j]

print(data)