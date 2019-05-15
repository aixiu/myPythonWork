#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
输入打印树冠的高度： 5
    #
   ###
  #####
 #######
#########
    #

分析如下：

第一行打 4个空格 1个#号
第二行打 3个空格 3个#号
第三行打 2个空格 5个#号
第四行打 1个空格 7个#号
第五行打 0个空格 9个#号

树冠的循环次数就是树树冠的高度
树冠空格以1递减，#号以2递增
树杆的打印，空格4，#号1个，和树冠第一层一样
'''

treeheight = int(input('输入打印树冠的高度： '))   #树冠高高

sapces = treeheight - 1    # 打印树冠空格数

hashes = 1    #打印树冠 #号数

treez = treeheight -1 #树桩空格数

while treeheight != 0:
    for i in range(sapces):
        print(' ' , end='')
    for i in range(hashes):
        print('#' , end='')
    print()  # 每一行打完最后换行

    sapces -= 1

    treeheight -= 1

    hashes += 2

# 这以下，打印树桩，for 循环打印空格数   先打空格，再打#号
for i in range(treez):
    print(' ',end='')
    
print('#')