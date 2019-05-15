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
        return '{}, {}, {}'.format(self.first + ' ' + self.surname, 
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


class Writer(Employee):
    raiseAmount = 1.08

    def __init__(self,first, surname, salary, masterwork):
        Employee.__init__(self, first, surname, salary)
        self.masterwork = masterwork
    
    def infoSummary(self):
        return '{}, {}, \n{}, \n{}'.format(self.first + ' ' + self.surname, 
        self.salary, self.email, self.masterwork)
    
    @classmethod
    def newFromString(cls, empstr):
        first, surname, salary, masterwork = empstr.split('-')
        return cls(first, surname, salary, masterwork)

class leader(Employee):
    def __init__(self,first, surname, salary, employees=None):
        super().__init__(first, surname, salary)
        # uper关键字也有两种意义：–调用父类的方法–调用父类的构造器
        # 但是，super并不表示一个指向对象的引用，它只是一个特殊的关键字，
        # 用来告诉编译器，现在要调用的是父类的方法。
        if employees is None:
            self.employess = []
        else:
            self.employess = employees

    def infoSummary(self):
        nameList = []
        for e in self.employess:
            nameList.append(e.first + ' ' + e.surname)
        return '{}, {}, \n{}, \n{}\n'.format(self.first + ' ' + self.surname, 
        self.salary, self.email, nameList)

    def addEmp(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)

    def delEmp(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)

    @classmethod
    def newFromString(cls, empstr):
        print('\nSorry, it doesnot work\n')


employee1 = Employee('Harry', 'Potter', 4000)

empCharacter1 = Employee('Harry', 'Potter', 4000)
empCharacter2 = Employee('Bilbo', 'Baggins', 6000)

employee1 = Employee('Harry', 'Potter', 4000)

empStr1 = 'J.K-Rowling-10000-Harry Potter'
empStr2 = 'J.R.R-Tolkien-8000-The adventure of Tom Sawyer'

empWriter1 = Writer('Mark Twain', 'Baggins', 6000, 'The adventure of Tom Sawyer')

empLeader = leader('Julius', 'Caesar', 1200, [empCharacter1, empCharacter2])

empLeaderC = leader.newFromString(empStr1)

# print(employee1.infoSummary())

# employee1.raiseSalary()
# print(employee1.infoSummary())

# employee1.raiseAmount = 1.08
# employee1.raiseSalary()
# print(employee1.infoSummary())

# Employee.setRaiseAmount(1.07)
# print(employee1.raiseAmount)



empWriter3 = Writer.newFromString(empStr1)
# print(employee3.infoSummary())
# print(empWriter3.infoSummary())
# print(empWriter1.raiseAmount)

# print(empLeader.infoSummary())
print(empLeader.infoSummary())

empLeader.addEmp(empWriter1)

print(empLeader.infoSummary())

empLeader.delEmp(empWriter1)

print(empLeader.infoSummary())
# from datetime import date, timedelta

# day = date.today() + timedelta(days= 0)
# Employee.whatDay(day)



