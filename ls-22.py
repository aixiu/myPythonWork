#!/usr/bin/env python
# -*- coding: utf-8 -*-

# def spam(divideBy):
#     return 42/divideBy

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# 以上代码出现 ZeroDivisionError: division by zero 错误。

# 修改如下：

# def spam(divideBy):
#     try:
#         return 42/divideBy
#     except ZeroDivisionError:
#         pass
#         # print('出错：0 不被接受')
#         # print('Error: Invalid argument')

# print(spam(2))
# print(spam(12))
# print(spam(0))
# print(spam(1))

# try 语句格式
# try:
#     pass
# except Exception:
#     pass
# else:
#     pass
# finally:
#     pass

# 例子
# try:
#     f = open('testfile.txt')
#     print(f.read())
# except Exception:
#     print('Sorry, this file does not exist')

# 例子二
# bad_var = 'I am nto bad_var'
try:
    var = bad_var
except NameError as e:  # 把系统出错内容写入E 然后打印出系统出错内容
    print(e)
else:
    print(var)
finally:
    print('Executing Finally...')


