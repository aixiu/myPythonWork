#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 游戏编程：按以下要求定义一只乌龟和鱼类并尝试编程
    # 假设游戏场景范围（x, y）为 0 <= x <= 10   0 <= y <= 10
    # 游戏生成1只乌龟和10条鱼
    # 他们的移动方向均随机
    # 乌龟的最大移动能力是2（乌龟可以随机选择移动是1还是2），鱼的最大移动能力是1
    # 当移动到场边缘，自动向反方向多动
    # 乌龟初始化体力为100（上限）
    # 乌龟每移动一次，体力消耗1
    # 当乌龟和鱼重叠，乌龟吃掉鱼，乌龟体力增加20
    # 鱼不计算体力
    # 当乌龟体力值为0或者鱼的数量为0时，游戏结束

import random as r   # as 给 random 起别名 r

# 定义乌龟类
class Turtle(object):
    def __init__(self):
        self.power =100   # 乌龟的初始体力

        # 初始化乌龟的们置
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    # 乌龟移动的方法
    def move(self):
        # 新的X坐标，用 choice()返回随机项。
        new_x = r.choice([-2, -1, 1, 2]) + self.x
        new_y = r.choice([-2, -1, 1, 2]) + self.y

        # 判读 乌龟的移动是否超出了边界 取反
        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x - 10)
        else:
            self.x = new_x


        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        self.power -= 1

        return self.x, self.y

    def eat(self):
        self.power += 20
        if self.power >= 100:
            self.power = 100

class Fish(object):

    def __init__(self):
        self.x = r.randint(0, 10)
        self.y = r.randint(0, 10)

    def move(self):
        new_x = r.choice([-1, 1]) + self.x
        new_y = r.choice([-1, 1]) + self.y

        if new_x < 0:
            self.x = 0 - (new_x - 0)
        elif new_x > 10:
            self.x = 10 - (new_x -10)
        else:
            self.x = new_x


        if new_y < 0:
            self.y = 0 - (new_y - 0)
        elif new_y > 10:
            self.y = 10 - (new_y - 10)
        else:
            self.y = new_y

        return self.x, self.y


turtle = Turtle()
fish = []
for i in range(10):
    new_fish = Fish()
    fish.append(new_fish)



while True:
    if not len(fish):
        print('鱼被吃完了，游戏结束')
        break
    if not turtle.power:
        print('乌龟没有体力了，游戏结束')
        break

    pos = turtle.move()   # 乌龟每次移动后的坐标

    # 在迭代中做列表的删除元素是非常危险的，经常会出现一些意到的问题因为迭代器是直接引用
    # 列表元素的数据做的操作，所以这里把列表拷贝一份传给迭代器，然后再对原列表做操作

    for each_fish in fish[:]:
        if each_fish.move() == pos:
            turtle.eat()
            fish.remove(each_fish)
            print('有一条鱼被吃掉了')
