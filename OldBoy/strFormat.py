#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 字符串拼接，最好用.format方式，其次用%s方式，最好不要用‘+’号，
# 万恶的‘+’，会把每个符符串都开辟内存空间，不高效！
name = input('name: ').strip()  # .strip() 
age = input('age: ').strip()
job = input('job: ').strip()

print('InFomation of \n{}\n{}\n{}\n'.format(name, age, job))

# 函数原型 
# 声明：s为字符串，rm为要删除的字符序列 
# s.strip(rm) :删除s字符串中开头、结尾处，位于 rm删除序列的字符 
# s.lstrip(rm) :删除s字符串中 开头处，位于 rm删除序列的字符 
# s.rstrip(rm) :删除s字符串中 结尾处，位于 rm删除序列的字符