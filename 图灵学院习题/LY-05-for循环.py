#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
*
* *
* * *
* * * *
* * * * *
'''

# 打印上边的图形
    # while 循环

treeheight = int(input('输入打印的高度： '))   #高度
hashes = 1 

while treeheight != 0:
    for i in range(hashes):
        print('*',end=' ')
    print()
    treeheight -= 1
    hashes += 1
    

    # for 循环
treeheight = int(input('输入打印的高度： '))   #高度
for i in range(treeheight):
    for j in range(i + 1):
        print('*',end=' ')
    print()


'''
*
* *
*   *
*     *
* * * * *
'''

# 打印上边的图形
    # for 循环

for i in range(5):
    for j in range(i + 1):
        if i == 4:
            print('*',end=' ')
            continue
        elif j == 0 or j == i:
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()


# 打印倒三角
'''
* * * * *
* * * * 
* * * 
* * 
* 
'''

# i 控制行号
# j 控制列号

    # 例一
for i in range(5):
    for j in range(5 - i):  # 可以实现反向
        print('*',end=' ')
    print()

    #例二，改进
    # 可以使用参数控制 range 结果
for i in range(5, 0, -1):
    for j in range(i, 0, -1):  # 可以实现反向
        print('*',end=' ')
    print()



# 打印正三角形
    #     *
    #    * *
    #   * * *
    # * * * * *

# i-for 控制行
# j-for 控制列

for i in range(6):
    # 总体思路是，先打印空格，再打印星星。
    for j in range(6 - i):
        print('',end=' ')
    for m in range(i + 1):
        print('*', end=' ')
    print()

