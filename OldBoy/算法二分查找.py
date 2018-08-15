#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 递归函数的实例
# 给定一个列表，查找某数值在不在该列表中

def bin_search(data_sou, find_n):
    mid = int(len(data_sou)/2)    # 比如：int(3.6) 结果为：3
    if len(data_sou) >= 1:
        if data_sou[mid] > find_n:   # 要找的数小于中间值，那么数据在中间值左边
            print('要找的数据在 [{}] 左边'.format(data_sou[mid]))
            print(data_sou[:mid])
            bin_search(data_sou[:mid], find_n)
        elif data_sou[mid] < find_n:  # 要找的数大于中间值，那么数据在中间值右边
            print('要找的数据在 [{}] 右边'.format(data_sou[mid]))
            print(data_sou[mid:])
            bin_search(data_sou[mid:], find_n)
        else:
            print('找到数据 >>> [{}] <<<'.format(data_sou[mid]))
    else:
        print('\n{:=^30}'.format('傻逼了吧，什么也没找到'))

if __name__ == '__main__':
    data = list(range(1, 600))
    bin_search(data, 1)

# if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时，if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，if __name__ == '__main__'之下的代码块不被运行。