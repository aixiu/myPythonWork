#!/usr/bin/env python
# -*- coding: utf-8 -*-


heine = open('heine.txt')
poem = heine.read()
print(poem)
print(heine.closed)
heine.close()
print(heine.closed)

# 以上方法中，有 open() 打开，必须要用 .close() 关闭。

# 用 with open as 方法打开，语句块结束，文件自动关闭。
with open('heine.txt',mode='a') as heine:
    heine.write('\nForm Heine')

with open('heine.txt',mode='r') as heine:
    print(heine.read())