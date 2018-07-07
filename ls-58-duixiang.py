#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random   # 随机数函数
import math   # 数学运算模块
import time
#剑客
class Warriors:

    def __init__(self, name, Kungfu, attkMax, defendMax):
        self.name = name
        self.energyValue = Kungfu
        self.attkMax = attkMax
        self.defendMax = defendMax

    def attack(self):
        return self.attkMax * (random.random() + 0.5)

    def defend(self):
        return self.defendMax * (random.random() + 0.5)

# 比武
class Battles:
    def launchAtack(self, warrior1, warrior2):

        while True:

            if self.fight(warrior1, warrior2) == 'Game over':
                print('Game over')
                break
            if self.fight(warrior2, warrior1) == 'Game over':
                print('Game over')
                break

    @staticmethod
    def fight(warriorA, warriorB):

        attkAmount = warriorA.attack()
        defendAmount = warriorB.defend()

        damage2warriorB = math.ceil(attkAmount - defendAmount)
        warriorB.energyValue = warriorB.energyValue - damage2warriorB

        time.sleep(1)
        print('\n{}进攻, {}防守\n这次过招的伤害值{}\n{}的战斗力下降到{}\n'.format(
            warriorA.name, warriorB.name, damage2warriorB, warriorB.name, warriorB.energyValue))

        if warriorB.energyValue <= 0:
            return 'Game over'
        else:
            return 'Continue fight'

blowSonw = Warriors('西门吹雪', 50, 20, 10)
loneCity = Warriors('夜孤城', 50, 20, 10)

forbiedenCity = Battles()
forbiedenCity.launchAtack(blowSonw, loneCity)
