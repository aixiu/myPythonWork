#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 记录程序Debug解决方案
import logging

# 此句添加后所有的DEBUG信息都不显示。
# logging.disable(logging.CRITICAL)  

# debug等级为DEBUG，记录时间，等级，信息等。
# logging.basicConfig(level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

# 可以把所有DEBUG内容写入文件，格式如下：
logging.basicConfig(filename = 'myProgramLog.txt', level = logging.DEBUG, format = '%(asctime)s - %(levelname)s - %(message)s')

def factorial(n):
    logging.debug('Start of factorial({})'.format(n))

    total = 1

    for i in range(n+1):   # 参数不能从0开始，换 for i in range(1,n+1): 后正常
        total *= i
        logging.debug('i is {}, total is {}'.format(i, total))

    logging.debug('End of factorial({})'.format(n))
    return total

print(factorial(5))
logging.debug('End of program')