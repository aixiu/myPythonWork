#!/usr/bin/env python
# -*- coding: utf-8 -*-

# def login(func):
#     def inner(namehaha):
#         print('{:=^30}'.format('密码验证成功'))
#         return func(namehaha)
#     return inner

# @login
# def home(name):
#     print('Welcome [{}] to Home page'.format(name))    

# # home = login(home)
# home('aixiu')


# 调用新的home()相当于调用inner()，所以inner要接收home传过来的实参'aixiu'，
# inner必须要有一个形参'namehaha'（形参名字可以自己定义），接下来，func相当于home,
# 也必须有参数，且形参名字和inner形参一至。

# 参数传递：home()的参数传给了inner()，函数 inner 把参数传递给内部 func 进行调用，
# 由于此时 inner相当于 home 所以func也应该接收参数，参数数量和传入的参数一至
# 即：inner 要定义一个接收 home 传过过来的形参，
# 由于 func 相当于 home 且inner接收到的参数传递给 func进行调用 所以 func 的形参和inner一致

# @login 作用：
# 
# 第一步，先将 @login 下边的函数名 home ，
# 其实就是内存地址，做为参数传给了logo(func)的 func
# 即把整个home函数当作参数传给了login  
# 所以，内部就会去执行 inner 函数，最终返回login内部函数 inner 内存地址  
# inner 接受 func 函数传进来的参数，并传递给 下边 func调用
#  
# 第二步，再将login返回的函数内存地址 inner
# 重新赋值给了 @login 下边的函数名 home ,此时 home 函数,已经不是原来的 home 函数，而是一个新的 home 
# 即：home = login(home) 所以最后调用 home() 时方法不变，却增加了函数 inner 里边的功能。


# 有多个不同参数的调用案例

# def login(func):
#     def inner(*args, **kwargs):
#         print('{:=^30}'.format('密码验证成功'))
#         return func(*args, **kwargs)  # 此处的返回值效果，见下 home 函数 
#     return inner

# @login
# def home(name, passed):
#     print('Welcome [{}] to Home page'.format(name))
#     return 'ok'    # 此处如果有返回值，那么，inner 函数必须 return func 才有效果

# @login
# def tv(name):
#     print('Welcome [{}] to Home page'.format(name))

# # home = login(home)
# t = home('aixiu', 'haha')   # 返回值需用 print 打印出来。直接运行函数是不显示返回值的
# print(t)
# tv('aixiu')


# @login 装饰器自身带参数的案例

def log(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('execute')
def now(name):
    print('2015-3-25')

now('aixiu')

#  详解
# 和两层嵌套的decorator相比，3层嵌套的效果是这样的：
# 首先执行log('execute')，返回的是decorator函数，
# 此时相当于 由 @log('execute')变成为 @ decorator  (此时差不多和不带变量的装饰器差不多了)
# 再调用返回的函数，参数是now函数，
# 返回值最终是wrapper函数。


# 视频地址：  http://edu.51cto.com/center/course/lesson/index?id=89993    20分钟左右