#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Role(object):
    def __init__(self, name, role, weapon, life_value):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_val = life_value

    def buy_weapon(self, weapon):
        print('{} is buying [{}]'.format(self.name, weapon))
        self.weapon = weapon


p1 = Role('SanJiang', 'Police', 'B10', 90)
t1 = Role('ChunYun', 'Terrorist', 'B11', 100)

p1.buy_weapon('AK47')
t1.buy_weapon('B51')

print('P1:', p1.weapon)
print('t1:', t1.weapon)