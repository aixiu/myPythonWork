#!/usr/bin/env python
# -*- coding: utf-8 -*-

def login(func):
    def inner(namehaha):
        print('{:=^30}'.format('密码验证成功'))
        return func(namehaha)
    return inner

@login
def home(name):
    print('Welcome [{}] to Home page'.format(name))
    
# def tv(name):
#     print('Welcome {} to TV page'.format(name))

# def moive(name):
#     print('Welcome {} to Movie page'.format(name))
# home = login(home)
home('aixiu')
s = home.__name__
print(s)

# 调用新的home()相当于调用inner()，所以inner要接收home传过来的实参'aixiu'，
# inner必须要有一个形参'namehaha'（形参名字可以自己定义），接下来，func相当于home,
# 也必须有参数，且形参名字和inner形参一至。