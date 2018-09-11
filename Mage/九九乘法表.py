#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 九九乘法表例子 最原始的办法。

# for i in range(1,10):
#     s = ''
#     for j in range(1,10):
#         if j < i + 1:   # 此处判断，是只取左下角的部分，如果不加判断，则显示一个正方形方阵
#             s += str(j) + '*' + str(i) + '=' + str(i*j) + ' '
#     print(s)

# 九九乘法表例子 进阶，即然J要用I来做限制，则可以把j的 range(1,10)改为(1,i+1)
# for i in range(1,10):
#     s = ''
#     for j in range(1,i+1):        
#         s += str(j) + '*' + str(i) + '=' + str(i*j) + ' '
#     print(s)


for i in range(1,10):
    for j in range(1,i+1):        
        print('{} * {} = {}  '.format(j, i ,i*j), end='')
    print()