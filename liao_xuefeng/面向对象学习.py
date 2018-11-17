
#!/usr/bin/env python
# -*- coding: utf-8 -*-

std1 = {'name': 'Michael', 'score': 98}
std1 = {'name': 'Bob', 'score': 81}

def print_score(std):
    print('%s: %s' %(std['name'], std['score']))


print(print_score(std1))