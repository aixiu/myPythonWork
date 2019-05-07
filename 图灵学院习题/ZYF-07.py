#!/usr/bin/env python
# -*- coding: utf-8 -*-

# append(), extend(), insert()

a = [1, 2, 3, 4, 5]
a.append([6, 7, 8])
print(a)

b = [1, 2, 3, 4, 5]
b.extend([6, 7, 8])
print(b)

c = [1, 2, 3, 4, 5]
c.insert(3, 10)
print(c)