#!/usr/bin/env python
# -*- coding: utf-8 -*-


sum = 0
for i in range(101):
    sum += i
print(sum)

print('%2d-%02d' % (3, 1))
print('%.2f' % 3.1415926)


L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]

print(L[0][0])
print(L[1][1])
print(L[2][2])