#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time

# print(time.time())

# 例一  1到100000的积，所用的时间
def calcProd():
    product = 1
    for i in range(1,100000):
        product *= i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()

print('最终结果一共有 {} 位数'.format(len(str(prod))))
print('总共用时 {:.2f} 秒'.format(endTime - startTime))

# 例二
# time.sleep()  # 暂停给定秒数后执行程序。该参数可以是一个浮点数来表示一个更精确的睡眠时间。

# for i in range(3):
#     print('aixiu')
#     time.sleep(1)
#     print('aixiu')
#     time.sleep(1)

# 例三

# now = time.time()
# print(now)
# print(round(now, 2))
# print(round(now, 4))
# print(round(now))