#!/usr/bin/env python
# -*- coding: utf-8 -*-

# os - 操作系统相关

# 跟操作系统相关，主要是文件操作
# 与系统相关的操作，主要包含在三个模块里
    # os， 操作系统目录相关
    # os.path, 系统路径相关操作
    # shutil， 高级文件操作，目录树的操作，文件赋值，删除，移动
# 路径：
    # 绝对路径： 总是从根目录上开始
    # 相对路径： 基本以当前环境为开始的一个相对的地方


# os 模块
import os
# getcwd() 获取当前的工作目录
# 格式：os.getcwd()
# 返回值：当前工作目录的字符串
# 当前工作目录就是程序在进行文件相关操作，默认查找文件的目录

mydir = os.getcwd()
print(mydir)

print(os.sep)
print(os.pardir)