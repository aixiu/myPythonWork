#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个利用unicode的加密和解密的小游戏，限定大写字母
# 对输入的字符进行转换成unicode编码，然后再转换成原始信息

message = input('输入要加密的字符串>>> ')

secmessage = ''

for i in message:
    if i.isalpha():
        secmessage += str(ord(i) - 23)
    elif i.isspace():
        secmessage += str(ord(i))

print('加密后的信息为>>> ',secmessage)

normmessage = ''

for i in range(0, len(secmessage)-1,2):
    charCode = secmessage[i] + secmessage[i+1]
    print(charCode)
    if charCode != '32':
        normmessage += chr(int(charCode) + 23)
    else:
        normmessage += chr(int(charCode))

print('还原码为>>> ',normmessage)