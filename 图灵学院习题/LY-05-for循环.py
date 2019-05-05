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
for i in range(treeheight + 1):
    for j in range(i):
        print('*',end=' ')
    print()

