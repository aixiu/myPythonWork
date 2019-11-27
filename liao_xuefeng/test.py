#!/usr/bin/env python
# -*- coding: utf-8 -*-


# L1 = ['Hello', 'World', 18, 'Apple', None]
# L2 = [s.lower() for s in L1 if isinstance(s, str)]

# print(L2)
# if L2 == ['hello', 'world', 'apple']:
#     print('测试通过!')
# else:
#     print('测试失败!')

# ----------------------------------------------

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# fib(6)

# ------------------------------------

# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         yield b
#         a, b = b, a + b
#         n = n + 1
#     return 'done'

# for i in fib(6):
#     print(i)

# ---------------------------------------------

# l = list(filter(lambda n: n % 2 == 0, range(1, 20)))
# print(l)

# import time 

# def test():
#     time.sleep(2)
#     print("test is running!")

# def deco(func):  
#     start = time.time()
#     func() #2
#     stop = time.time()
#     print(stop-start)

# deco(test) #1


import time

def timer(func): #5
    def deco():  
        start = time.time()
        func()
        stop = time.time()
        print(stop-start)
    return deco
@timer
def test():
    time.sleep(2)
    print("test is running!") 



test() #7


def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

fib(10)