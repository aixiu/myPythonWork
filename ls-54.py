#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 类和对象的基础知识

# class Obj:
#     def __init__(self):
#         print(1)
# obj = Obj() #这时候__init__这个函数会被调用，self指obj这个对象。

# 具体实例
class Employee(object):

    raiseAmount = 1.04
    employeeNum = 0

    def __init__(self,first, surname, salary):
        self.first = first
        self.surname = surname
        self.salary = salary
        self.email = first + '.' + surname + '@PythonABC.com'

        Employee.employeeNum += 1
    
    def infoSummary(self):
        return '{}. {}. {}'.format(self.first + ' ' + self.surname, 
        self.salary, self.email)

    def raiseSalary(self):
        self.salary = self.salary * self.raiseAmount

    @classmethod
    def setRaiseAmount(cls, amout):
        cls.raiseAmount = amout

    @classmethod
    def newFromString(cls, empstr):
        first, surname, salary = empstr.split('-')
        return cls(first, surname, salary)

    @staticmethod
    def whatDay(day):
        num = day.weekday()
        if num == 0:
            print('\nLet\'s look at the bright side.')
        if num == 1:
            print('\nThank goodness monday is gone.')
        if num == 2:
            print('\nIt\'s wednesday.')
        if num == 3:
            print('\nHappy thursday!')
        if num == 4:
            print('\nHello friday, where have you been all week?')
        if num == 5:
            print('\nSaturday is the perfect day for a...')
        if num == 6:
            print('\nOn this lovely sunday...')


employee1 = Employee('Harry', 'Potter', 4000)

# print(employee1.infoSummary())

# employee1.raiseSalary()
# print(employee1.infoSummary())

# employee1.raiseAmount = 1.08
# employee1.raiseSalary()
# print(employee1.infoSummary())

# Employee.setRaiseAmount(1.07)
# print(employee1.raiseAmount)

empStr1 = 'J.K-Rowling-10000'
empStr2 = 'J.R.R-Tolkien-8000'

employee3 = Employee.newFromString(empStr1)
# print(employee3.infoSummary())

from datetime import date, timedelta

day = date.today() + timedelta(days= 0)
Employee.whatDay(day)



