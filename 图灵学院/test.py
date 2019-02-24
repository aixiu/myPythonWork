#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Person():
    def fget(self):
        return self.name*2
    def fset(self,name):
        self.name=name.upper()
        return self.name
    def fdel(self):
        self.name="Noname"
        return self.name
    # name=property(fget,fset,fdel,'...')
p1=Person()
p1.name='tl'

print(p1.name)
print(p1.fget())
print(p1.fdel())

tt = p1.fset('haha')
print(tt)
