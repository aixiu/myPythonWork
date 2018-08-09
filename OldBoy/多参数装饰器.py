#!/usr/bin/env python
# -*- coding: utf-8 -*-

  
def Before(request,kargs):
    print('before')
    # return 'Ok'
      
def After(request,kargs):
    print('after')
    # return 'No'
  
  
def Filter(before_func,after_func):
    def outer(main_func):
        def wrapper(request,kargs):
              
            before_func(request,kargs)          
              
            main_func(request,kargs)          
              
            after_func(request,kargs)            
              
        return wrapper
    return outer
      
@Filter(Before, After)
def Index(request,kargs):
    print('index')
    # return('haha')

Index('aixiu', 'jiaojiao')


# 解释
#  最主要的一句话：  @Filter(Before, After)  带参数后，其实就是先执行 除 @  符号外的该函数，
# 即 Filter(Before, After) 得到返回值后 ，
# 其实就是变成了 @Filter(Before, After) = @outer  不带参数的用法了


# @Filter(Before, After) 会选 执行 Filter(Before, After) 函数 会先忽略 @ 符号
# Filter(Before, After) 函数下边的子函数没有调用不会执行，Filter只会有一个返回值，即 outer 
# 加上 @ 符号 那么 @Filter 就相当于是 @outer 
# @outer 会把返回值 wrapper 重新赋值给 index 这里就和普通的装饰器一样的理解了。
# index 函数 等于 新的 index 函数，新的index 函数就是 wrapper 函数

# Filter(before_func,after_func) 函数接收到的两个函数参数，就是事先写好的两个
# Before和After 函数，并由Filter(Before, After) 传递给了 Filter


# http://edu.51cto.com//center/course/lesson/index?id=89980  40-50分钟左右，有讲解