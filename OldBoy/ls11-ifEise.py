#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 例一  if else
# while True:

#     sex = input('input you gender:')

#     if sex == 'girl':
#         print('I would like to have a little monkey')
#         break
#     elif sex == 'men':
#         print('Going to Gey')
#         break
#     else:
#         print('Pervert')
#         continue

# 例二 猜数字大小 
# num = 6

# while True:

#     aixiu = int(input('输入10以内数字>>> '))
#     if aixiu < num:
#         print('你输入的数小了')
#     elif aixiu > num:
#         print('你输入的数大了')
#     else:
#         print('Bingo')
#         break


# 例三 不用Break的方法

num = 6
aixiu = 1

while aixiu != num:   

    aixiu = int(input('输入10以内的数字>>> ')) 

    if aixiu < num:
        print('你输入的数小了')
    elif aixiu > num:
        print('你输入的数大了')

print('bingo')