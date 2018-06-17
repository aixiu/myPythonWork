#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 一个发邮件的实例。

customer = []

while True:
    createEntry = input('Enter customer(yes/no)?')
    createEntry = createEntry[0].lower()  # 换字符串中所有大写字符为小写

    if createEntry == 'no':
        break
    else:
        fName, lName, gender = input('Enter custer\'s name&gender: ').split()
        customer.append({'fName':fName,'lName':lName,'gender':gender})

for cust in customer:
    if cust['gender'] == 'male':
        title = 'Mr'+ cust['lName']
    else:
        title = 'Ms'+ cust['lName']

    print('''Dear {},
    As our distinguished customer,you......
    '''.format(title))