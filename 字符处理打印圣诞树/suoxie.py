#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 这是一个输入任意英文语句，输出为每个单词首字母，并且大写。

str = input('请输入一行英文语句，不用写标点! >>> ').upper()   
# 输入一行英文语句，并将小写字母转化成大写

listWords = str.split()    
# 用.split()方法，将传入进来的字符串以空格进行分割，并赋值给listWords

for i in listWords:     
    # 循环字符串listWords
    print(i[0],end='')   
    # 获取每个字符串首字母，以空字符进行拼接。  end=""  方法默认值是换行。