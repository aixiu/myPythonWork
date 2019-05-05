#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 设计一个验证用户密码的程序，用只有三次机会输入错误，不过如果用户输入的内容包括 “*” 则不计算在内

password = 'abc012'
times = 3
while times:
    input_password = input('请输入密码：')

    if '*' in input_password:
        print('密码中不能包含“*”号')
    else:
        if input_password == password:
            print('密码正确')
            break
        else:
            print('密码错误')
            times -= 1


# 改进版

password = 'abc012'
times = 3
while times:
    input_password = input('请输入密码：')

    if '*' in input_password:
        print('密码中不能包含“*”号')
    elif input_password == password:
        print('密码正确')
        break
    else:
        print('密码错误')
        times -= 1
else:
    print('次数用光了')
