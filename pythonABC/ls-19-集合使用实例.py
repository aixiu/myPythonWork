#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 野餐策划，统计拿东西的类别和数量


allGuests = {'Alice':{'apples': 5, 'pretzel': 12},
            'Bob':{'ham sandwiches': 3,'apples': 2},
            'Carol':{'cups': 3 ,'apples pies': 1}}


def totalBrought(guests, item):
    numBrought = 0
    for v in guests.values():
        numBrought += v.get(item, 0)
    return numBrought

# print('Number of things being brought: \n')
# print('-Apple             {}'.format(totalBrought(allGuests, 'apples')))
# print('-Cups              {}'.format(totalBrought(allGuests, 'cups')))
# print('-Pretzel           {}'.format(totalBrought(allGuests, 'pretzel')))
# print('-Ham sandwiches    {}'.format(totalBrought(allGuests, 'ham sandwiches')))
# print('-Apple Pies        {}'.format(totalBrought(allGuests, 'apples pies')))



# 使用集合的方法

foodSet =  set()
for v in allGuests.values():
    foodSet |= set(v)

print('Number of things being brought: \n')
for food in foodSet:
    print('-{:15}               {}'.format(food, totalBrought(allGuests, food)))