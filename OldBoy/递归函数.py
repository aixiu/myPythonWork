#!/usr/bin/env python
# -*- coding: utf-8 -*-

def calc(n):
    print(n)
    if n/2 > 1:
        return calc(n/2)

calc(10)