#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 迭代器&生成器

# names = iter(['alex', 'jack', 'list'])
# print(names)

# print(names.__next__())
# print(names.__next__())
# print(names.__next__())

def cash_money(amount):
    while amount > 0:
        amount -= 100
        yield '取了100块'
        print('又来取钱了！')

atm =  cash_money(500)
print(atm.__next__())
print('干点别的事')
print(atm.__next__())
print(atm.__next__())



