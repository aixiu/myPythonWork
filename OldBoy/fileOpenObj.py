#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pathlib import Path

# f = open('./OldBoy/test.log','w')

# f.write('This is the first line\n')
# f.write('This is the second line\n')
# f.write('This is the 3 line\n')
# f.write('This is the 4 line\n')

# f.close()



f = open('./OldBoy/test.log','r')

for line in f:
    print(line.strip())


f.close()
