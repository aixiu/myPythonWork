#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://ke.qq.com/webcourse/index.html#cid=134017&term_id=100150034&taid=1866936384359297&type=512&vid=a1423u4g56u
# 练习

class MyClass:
    x = 123

    def __init__(self):
        print('init')

    def foo(self):
        return 'foo = {}'.format(self.x)

a = MyClass()   # 实例化及初始化。
print(a.foo())