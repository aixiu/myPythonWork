#!/usr/bin/env python
# -*- coding: utf-8 -*-

treeheight = int(input('输入打印树冠的高度： '))   #树冠高高

sapces = treeheight - 1    # 打印空格数

hashes = 1    #打印#号数

treez = treeheight -1 #树桩高度

while treeheight != 0:
    for i in range(sapces):
        print(' ' , end='')
    for i in range(hashes):
        print('#' , end='')
    print()

    sapces -= 1

    treeheight -= 1

    hashes += 2

for i in range(treez):
    print(' ',end='')
    
print('#')