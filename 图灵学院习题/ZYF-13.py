#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一个门票系统
    # 门票的原价是100元
    # 当周末的时候，门票涨价20%
    # 小孩子半票
    # 计算2个成人和1个小孩的平日票价

# 创建购票系系 Ticket
class Ticket(object):
    # weekend 周未， child 小孩
    def __init__(self, weekend=False, child=False):
        # 原价门票
        self.exp = 100
        if weekend:
            self.inc = 1.2  # 如果是周未涨20%
        else:
            self.inc = 1

        if child:
            self.discount = 0.5   # 如果小孩则半价
        else:
            self.discount = 1

    # 计算票价函数  num=购票数
    def cal_price(self, num):
        return self.exp * self.inc * self.discount * num

# 实例化大人和小孩
    #因为要计算两大小，一小时，平日的价，所以大人这：不涨价且全票，不用传产参数
adult = Ticket()   
child = Ticket(child=True)

print('两个成年人和一个小孩平日的价格是{}元'.format(adult.cal_price(2) + child.cal_price(1)))

print('{:=^30}'.format('华丽的分割线'))
adult = Ticket(weekend=True)   
child = Ticket(weekend=True, child=True)

print('两个成年人和一个小孩周未的价格是{}元'.format(adult.cal_price(2) + child.cal_price(1)))