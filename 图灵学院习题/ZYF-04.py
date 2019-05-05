#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个程序，打印出 0-100 所有奇数。
# ls = range(0, 101)
# for i in ls:
#     if i % 2 == 1:
#         print(i)

# 爱因斯坦曾出过这样一道数学题：有一条长阶梯，若每步跨2阶，最后剩下1阶；若每步跨3阶，
# 最后剩下2阶；若每步跨5阶，最后剩下4阶。若每步跨6阶，则最后剩下5阶。只有每步跨7阶，才刚好跨完。
    # 编写程序求该阶梯至少有多少阶

x = 0
while x < 1000:
    if(x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5) and (x % 7 == 0):
        print(x)
        break
    else:
        x += 1
else:
    print('结束')


# 如果打印出1000以内所有的符合的数则改动如下
x = 0
while x < 1000:
    if(x % 2 == 1) and (x % 3 == 2) and (x % 5 == 4) and (x % 6 == 5) and (x % 7 == 0):
        print(x)
        x += 1
        # break
    else:
        x += 1
else:
    print('结束')