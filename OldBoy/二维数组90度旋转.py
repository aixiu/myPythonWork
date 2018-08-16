#!/usr/bin/env python
# -*- coding: utf-8 -*-

data=[[col for col in range(4)] for row in range(4)]

 

for row in data:

    print(row)

print("-------------------------------------------")

# 方法一
# 此方法是根据，每次替换时，第1个数据是不变的。
# for i in range(len(data)):                                #外层循环  
#     for j in range(i+1,len(data)):                        #内层循环  
#         temp=data[i][j]                                   #数据交换
#         data[i][j]=data[j][i]  
#         data[j][i]=temp
         
# for n in data:print (n)


# 方法二
# 说明： enumerate()是python的内置函数，同时获得索引和值
for i, row in enumerate(data):
    for j in range (i ,len(row)):

        temp = data[j][i]
        data[j][i] = row[j]
        data[i][j] = temp

for r in data:print(r)





