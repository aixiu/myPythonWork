#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random   # 随机数模块

#剑客
class Warriors:

    def __init__(self, name, Kungfu, attkMax, defendMax):
        self.name = name
        self.energyValue = Kungfu
        self.attkMax = attkMax
        self.defendMax = defendMax

    # 攻击力
    def attack(self):
        return self.attkMax * (random.random() + 0.5)

    # 防御力
    def defend(self):
        return self.defendMax * (random.random() + 0.5)

# 比武
class Battle:

    def launchAtack(self, warrrior1, warrior2):

        while True:

            if self.fight(warrrior1, warrior2) == 'Game over':
                print('Game over')
                break
            if self.fight(warrrior2, warrior1) == 'Game over':
                print('Game over')
                break


    @staticmethod
    def fight(warriorA, warriorB):

        attkAmount = warriorA.attack()
        defendAmount = warriorB.defend()

        damage2warriorB = attkAmount - defendAmount   # A对B的伤害值
        warriorB.energyValue = warriorB.energyValue - damage2warriorB  # 伤害值打完，B的战斗力值

        print('{}进攻, {}防\n, 本次过招的伤害值{}, {}的战斗力下降到{}'.format(
            warriorA.name, warriorB.name, damage2warriorB, warriorB.name, warriorB.energyValue))

        if warriorB.energyValue <= 0:
            return 'Game over'
        else:
            return 'Continue fight'

blowSnow = Warning('西门吹雪', 50, 20, 10)
loneCity = Warning('夜孤城', 50, 20, 10)

forbidenCity = Battle()
forbidenCity.launchAtack(blowSnow, loneCity)