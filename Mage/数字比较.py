#!/usr/bin/env python
# -*- coding: utf-8 -*-

# a = int(input('{}>>> '.format('请输入一个数A')))
# b = int(input('{}>>> '.format('请输入一个数B')))

# if a > b:
#     print('{:=^30}\n{}'.format('最大值是', a))
# elif a == b:
#     print('{:=^30}'.format('一样大'))
# else:
#         print('{:=^30}\n{}'.format('最大值是', b))



# 计算1000以内的被7整除的前20个数(for循环)

count = 0
for i in range(0,1000,7):
    print(i)
    count += 1
    if count == 20:
        break