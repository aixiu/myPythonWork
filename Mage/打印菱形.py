#!/usr/bin/env python
# -*- coding: utf-8 -*-

'''
打印如菱形

   *
  ***
 *****
*******
 *****
  ***
   *
'''

# for i in range(-3, 4):
#     if i < 0:
#         pre = -i
#     else:
#         pre = i
#     print(' ' * pre + '*' * (7 - pre * 2 ))


'''
打印如菱形

*******
 *****
  ***
   *
  ***
 *****
*******
'''
# n = 7 
# e = n // 2
# for i in range(-e, n-e):
#     pre = -i if i < 0 else i  # 三元表达式  条件为真时的结果 if 判段的条件 else 条件为假时的结果
#     print(' ' * (e - pre) + '*' * (2 * pre + 1))


'''
打印如下闪电

    *
   **
  ***
 *******
    ***
    **
    *

分析：
我们可以把闪电以最中间一行为间隔分为三部分： 
第一部分 最中间行以上一个直角三角形 
第二部分 中间打印一行* 
第三部分 中间行一下倒直角三角形
'''
# 方法一
for a in range(4):
    for c in range(a,4): #此处循环*前边的空格 每行递减
         print("", end=" ")
    for b in range(0,a): #循环“*” 每行递增
         print("*", end="")
    print("")
print("********")
for q in range(3):
    for e in range(3):#遍历3行3列的空格
         print(end=" ")
    for w in range(q,3):#倒三角：循环输出“*”每行递减
         print("*", end="")
    print(" ")

# 方法二
for a in range(-3,4):
    if a<0: #当a<0时输出直角三角形
        print(" "*(-a)+"*"*(4+a))
    elif a>0: #当a>0时输出那个倒三角
        print(" "*2,"*"*(4-a))
    else:
        print("*"*7) # 输出中间一行“*”