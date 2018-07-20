#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 例四 不用Break的方法  限定次数

# num = 6
# aixiu = 1
# guessCount = 0

# while  guessCount < 3:
#     # print('Guess num >>> {}'.format(guessCount)) 
#     aixiu = int(input('输入10以内的数字(只有三次机会)>>> ')) 

#     if aixiu < num:
#         print('你输入的数小了')
#     elif aixiu > num:
#         print('你输入的数大了')
#     else:
#         print('bingo')
#         break

#     guessCount += 1
    
# else:  # 循环正常退出时才走下边代码,不正常退出就不执行
#     print('\n三次机会用完，还是没猜出来，哈哈')


# 例五 FOR循环实例

num = 6
aixiu = 1


for i in range(3):
    # print('Guess num >>> {}'.format(guessCount)) 
    aixiu = int(input('输入10以内的数字(只有三次机会)>>> ')) 

    if aixiu < num:
        print('你输入的数小了')
    elif aixiu > num:
        print('你输入的数大了')
    else:
        print('bingo')
        break

    
else:  # 循环正常退出时才走下边代码,不正常退出就不执行
    print('\n三次机会用完，还是没猜出来，哈哈')
