#!/usr/bin/env python
# -*- coding: utf-8 -*-

def login(func):
    def inner(namehaha):
        print('{:=^30}'.format('密码验证成功'))
        return func(namehaha)
    return inner

# @login
def home(name):
    print('Welcome {} to Home page'.format(name))
    
# def tv(name):
#     print('Welcome {} to TV page'.format(name))

# def moive(name):
#     print('Welcome {} to Movie page'.format(name))
home = login(home)
home('aixiu')