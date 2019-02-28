#!/usr/bin/env python
# -*- coding: utf-8 -*-


# 变量作用域
# 变量由作用范围限制
# 分类：按照作用域分类
    # 全局(global): 在函数外部定义
    # 局部（local)：在函数内部定义
# 变量的作用范围：
    # 全局变量：在整个全局范围都有效
    # 全局变量在局部可以使用（即函数内部可以访问函数外部定义的变量）
    # 局部变量在局部范围可以使用
    # 局部变量在全局范围无法使用
# LEGB原则
    # L（Local）局部作用域
    # E（Enclosing function locale）外部嵌套函数作用域
    # G（Global module）函数定义所在模块作用域
    # B（Buildin）： python内置模块的作用域

a1 = 100

def fun():
    print(a1)
    print('I am in fun')
    a2 = 90

    print(a2)

print(a1)
fun()
print(a2)

# 提升局部变量为全局变量
    # 使用global
    # 案例如下

def fun():
    global b1
    b1 = 100
    print(b1)
    print('I am in fun')
    b2 = 90

    print(b2)


fun()
print(b1)
# print(b2)

# globals, locals函数
    # 可以通过globals和locals显示出局部变量和全局变量
    # 参看以下案例

# globals 和 locals 叫做内建函数
a = 1
b = 2
def fun(c, d):
    e = 111
    print('Local = {}'.format(locals()))
    print('Globals = {}'.format(globals()))

fun(100, 200)


# eval()函数
    # 把一个字符串当成一个表达式来执行， 返回表达式执行后的结果
    # 语法：
        # eval(string_code, globals=None, locals=None)

# exec()函数
    # 跟eval功能类似， 但是，不返回结果
    # 语法：
        # exec(string_code, globals=None, locals=None)

x = 100
y = 200
# 执行x+y
# z = x + y
z1 = x + y
z2 = eval("x+y")

print(z1)
print(z2)

# ------------------------

# exec示例
x = 100
y = 200
# 执行x+y
# z = x + y
z1 = x + y
# 1, 注意字符串中引号的写法
# 2. 比对exec执行结果和代码执行结果
z2 = exec("print('x+y:', x+y)")

print(z1)
print(z2)


# 递照明函数
    # 函数直接或者间接调用自身
    # 优点：简洁，容易理解
    # 缺点：对弟归深度有限制，消耗资源大
    # python 对递归深度有限制，超过限制报错。
    # 在写递归程序的时候，一定要注意结束条件。

# 递归调用深度限制代码

# -------------------------------------------------------
# 内部函数，不修改全局变量可以访问全局变量
# 内部函数，修改同名全局变量，则python会认为它是一个局部变量
# 在内部函数修改同名全局变量之前调用变量名称（如print sum），
# 则引发Unbound-LocalError
# 在程序中设置的sum属于全局变量,而在函数中没有sum的定义,根据python访问局部变量和全局变量的规则：
# 当搜索一个变量的时候，python先从局部作用域开始搜索，如果在局部作用域没有找到那个变量，
# 那样python就在全局变量中找这个变量，如果找不到抛出异常(NAMEERROR或者Unbound-LocalError，
# 这取决于python版本。)

# 如果内部函数有引用外部函数的同名变量或者全局变量,并且对这个变量有修改.
# 么python会认为它是一个局部变量,又因为函数中没有sum的定义和赋值，所以报错。
# -------------------------------------------------------

x = 0
def fun():
    global x
    x += 1
    print(x)
    # 函数调用自己
    fun()

# 调用函数
fun()


# 斐波那契额数列
# 一列数字，第一个值是1， 第二个也是1， 从第三个开始，每一个数字的值等于前两个数字出现的值的和
# 数学公式为： f(1) = 1,  f(2) = 1,  f(n) = f(n-1) + f(n-2)
# 例如： 1, 1，2，3, 5, 8, 13。。。。。。。。

# 下面求斐波那契数列函数有一定问题，比如n一开始就是负数，如何修正
# n表示求第n个数子的斐波那契数列的值