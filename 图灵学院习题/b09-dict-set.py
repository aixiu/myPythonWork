#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 写一个程序，来管理用于登陆系统的用户信息：登录名和密码。
# 登录用户帐号建立后，已存在用户可以用登录名和密码重返系统，新用户不能用别人的用户名
# 建立用户帐号


# 模拟从数据库里取出来的用户名和密码
user_pass = {'laotie':'password', 'huniu':'admin'}

def create_user(username,password):
    '''
    username:用户建立帐号的用户名
    password:用户建立帐号的密码
    '''

    # 判断用户输入帐号是不是已经在
    usernames = user_pass.keys()

    if username in usernames:
        print('用户名已经被注册了')
    else:
        #没有被注册，那么就更新我们的 user_pass
        user_pass[username] = password
        print('恭喜你，你已经成为我们的会员了')

# create_user('aixiu', 123)

# print(user_pass)


def login_user(username, password):
    #首先判断登录用户名是否存在

    usernames = user_pass.keys()

    if username not in usernames:
        print('你都还不是我们的会员')
    elif password != user_pass[username]:
        # 判断用户的密码是否正确
        print('密码错了')
    else:
        print('登录成功')

login_user('laotie', 'password')