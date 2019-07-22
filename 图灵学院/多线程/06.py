#!/usr/bin/env python
# -*- coding: utf-8 -*-

import time
import threading

def fun():
    print("Start fun")
    time.sleep(2)
    print("end fun")

print("Main thread")

t1 = threading.Thread(target=fun, args=() )
t1.start()

time.sleep(1)
# t1.join()
print("Main thread end")