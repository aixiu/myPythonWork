#!/usr/bin/env python
# -*- coding: utf-8 -*-
# import time
# def consumer(name):
#     print('{}准备吃包子啦！'.format(name))
#     while True:
#         baozi = yield
#         print('包子{}来了，被{}吃了！'.format(baozi, name))

# def producer():
#     c = consumer('A')
#     c2 = consumer('B')
#     c.__next__()
#     c2.__next__()
#     print('准备开始做包子啦！')
#     for i in range(10):
#         time.sleep(1)
#         print('做了2个包子！')
#         c.send(i)
#         c2.send(i)

# producer()

# send(i) 把参数传给了yield  同时复制给了baozi ，yield不光能反回值，还能接收sedn传过来的值
# yield想要接收到值，必须用send方法传


