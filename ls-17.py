#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 函数的定义及使用

# def allotEmail(firstNmae, surname):
#     return firstNmae + '.' + surname + '@pythonabc.org'

# name = input('Enter your name: ')
# fName, sName = name.split()
# compEmail = allotEmail(fName, sName)

# print('You company email: \n' , compEmail)



# 例二

# def mult_divide(num1, num2):
#     return (num1 * num2), (num1 / num2)

# mult,divide = mult_divide(5, 4)

# print('5 * 4 = ',mult)
# print('5 / 4 = ',divide)

# 例三

# def change_name():
#     name = 'aixiu'
#     return name

# print(change_name())


# 例三 素数测试

# def isprime(num):

#     for i in range(2, num):
#         if (num % i) == 0:
#             return False
#     return True

# aixiu = int(input('请输入一个数>>> '))

# print(isprime(aixiu))



# 例四  给定一个数，找出这个数之前的所有素数

def isprime(num):
    for i in range(2, num):
        if (num % i) == 0:
            return False
    return True

def getPrimes(numMax):
    primes = []

    for num1 in range(2, numMax):
        
        if  isprime(num1):
            primes.append(num1)

    return primes

maxNum = int(input('请输入一个数>>> '))

listOfPrimes = getPrimes(maxNum)

for prime in listOfPrimes:
    print(prime, end=' ')