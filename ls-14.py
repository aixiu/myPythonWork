#!/usr/bin/env python
# -*- coding: utf-8 -*-


message = input('输入要加密的字母:>>> ')

key = int(input('设置加密码算法数字(-26 ~ 26)>>> '))

secret_message = ''

for char in message:
    if char.isalpha():
        char_code = ord(char) + key
        
        if char.isupper(): 
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26

        if char.islower():
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        secret_message += chr(char_code)
    else:
        secret_message += char

print('加密后的信息为: ',secret_message)

# 解密

key = -key

orig_message = ''

for char in secret_message:
    if char.isalpha():
        char_code = ord(char) + key
        
        if char.isupper(): 
            if char_code > ord('Z'):
                char_code -= 26
            if char_code < ord('A'):
                char_code += 26

        if char.islower():
            if char_code > ord('z'):
                char_code -= 26
            if char_code < ord('a'):
                char_code += 26

        orig_message += chr(char_code)
    else:
        orig_message += char

print('解密后的信息为: ',orig_message)