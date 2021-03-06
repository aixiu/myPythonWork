#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 文件
    # 长久保存信息的一种数据信息集合
    # 常用操作
        # 打开关闭（文件一旦打开，需要关闭操作）
        # 读写内容
        # 查找 

# open函数
    # open函数负责打开文件，带有很多参数
    # 第一个参数： 必须有，文件的路径和名称
    # mode：表明文件用什么方式打开
        # r:以只读方式打开
        # w：写方式打开，会覆盖以前的内容
        # x：创建方式打开，如文件已经存在，报错
        # a：append方式，以追加的方式对文件内容进行写入
        # b： binary方式，二进制方式写入
        # t： 文本方式打开
        # +： 可读写


# 打开文件，用写的方式
# r表示后面字符串内容不需要转义
# f称之为文件句柄

f = open(r'test01.txt', 'w')
# 文件打开后必须关闭
f.close()

# 此案例说明，以写方式打开文件，默认是如果没有文件，则创建


# with语句
    # with语句使用的技术是一种成为上下文管理协议的技术(ContextManagementProtocal)
    # 自动判断文件的作用域，自动关闭不在使用的打开的文件句柄

# with 语句案例
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    pass
    # 下面语句块开始对文件f进行操作
    # 在本模块中不需要在使用close关闭文件f

# with 案例

with open(r'test01.txt', 'r', encoding='utf-8') as f: 
    # 如果是Windwos: 末尾设置 newline=''，新行为空。不加的话会行间距会自动加一行。
    # 按行读取内容
    strline = f.readline()
    # 此结构保证能够完整读取文件知道结束
    while strline:
        print(strline)
        strline = f.readline()


# list能用打开的文件作为参数，把文件内每一行内容作为一个元素

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # 以打开的文件f作为参数，创建列表
    l = list(f)
    for line in l:
        print(line)


# read是按字符读取文件内容
# 允许输入参数决定读取几个字符，如果没有指定，从当前位置读取到结尾
# 否则，从当前位置读取指定个数字符

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read()
    print(len(strChar))
    print(strChar)
    
# 作业：
# 使用read读取文件，每次读取一个，使用循环读完
# 尽量保持格式



# seek (offset, from)
    # 移动文件的读取位置，也叫读取指针
    # from 的取值范围：
        # 0：从文件开始偏移
        # 1：从文件当前位置开始偏移
        # 2：从文件末尾开始偏移
    # 移动的单位是字节（byte）
    # 一个汉字由若干个字节构成
    # 返回文件指针对当前位置

# seek案例
# 打开文件后，从第5个字节出开始读取

# 打开读写指针在0处，即文件的开头

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    # seek移动单位是字节
    f.seek(6, 0)   # 偏移量（步长）为4，从0处开始。
    strChar = f.read()
    print(strChar)


# 关于读取文件的练习
# 打开文件，三个字符一组读出内容，然后显示在屏幕上
# 每读一次，休息一秒钟

# 让程序暂停，可以使用time下的sleep函数
import time

with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(3)
    while strChar:
        print(strChar)
        time.sleep(0.5)
        strChar = f.read(3)



# tell函数： 用来显示文件读写指针的当前位置
with open(r'test01.txt', 'r', encoding='utf-8') as f:
    strChar = f.read(3)
    pos = f.tell()

    while strChar:
        print(pos)
        print(strChar)

        strChar = f.read(3)
        pos = f.tell()

# 以下结果说明：
# tell的返回数字的单位是byte
# read是以字符为单位



# 文件的写操作-write
    # write(str): 把字符串写入文件
    # writeline(str): 把字符串按行写入文件
    # 区别：
        # write函数参数只能是字符串
        # writerline参数可以是字符串，也可以是字符序列

    
# write 案例

# 1. 向文件追加一句诗
# a代表追加方式打开

with open(r'test01.txt', 'a',encoding='utf-8') as f:
    f.write('\n生活不仅有眼前的苟且\n还有远方的苟且')

# 可以直接写入行，用 writeline
# writelines表示写入很多行，参数可以是list格式

with open(r'test01.txt', 'a',encoding='utf-8') as f:
    f.writelines('\n还有远方的思念')
    f.writelines('\n等等')

l = ['I', 'love', 'wangxiaojing']
with open(r'test01.txt', 'a',encoding='utf-8') as f:
    f.writelines(l)



# 持久化 - pickle
    # 序列化（持久化，落地）：把程序运行中的信息保存在磁盘上
    # 反序列化： 序列号的逆过程
    # pickle： python提供的序列化模块
    # pickle.dump:序列化
    # pickle.load:反序列化


# 序列化案例
import pickle

age = 19
with open(r'test01.txt', 'wb') as f:
    pickle.dump(age, f)

# 反序列化案例

import pickle

with open(r'test01.txt', 'rb') as f:
    age = pickle.load(f)
    print(age)


# 序列化案例2

import pickle
a = [19, 'shendl', 'HOHO', [200, 50]]
with open(r'test01.txt', 'wb') as f:
    pickle.dump(a, f)

with open(r'test01.txt', 'rb') as f:
    a = pickle.load(f)

    print(a)


# 持久化-shelve
    # 持久化工具
    # 类似字典，用kv对保存数据，存取方式跟字典也类似
    # open, close


# 使用 shelve 创建文件并使用

import shelve

# 打开文件
# shv相当于一个字典
shv = shelve.open(r'shv.db')
shv['one'] = 1
shv['two'] = 2
shv['three'] = 3

shv.close()

# 通过以上案例发现，shelve自动创建的不仅仅是一个shv.db文件，
# 还包括其他格式文件

# shelve 读取案例

shv = shelve.open(r'shv.db')
try:
    print(shv['one'])
    print(shv['two'])
    print(shv['three'])
except Exception as e:
    print('还错么')
finally:
    shv.close()


# shelve特性
    # 不支持多个应用并行写入
        # 为了解决这个问题，open的时候可以使用flag=r
    # 写回问题
        # shelve情况下不会等待持久化对象进行任何修改
        # 解决方法： 强制写回：writeback=True

# shelve 之只读打开
import shelve

shv = shelve.open(r'shv.db', flag='r')

try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()




import shelve 

shv = shelve.open(r'shv.db')
try:
    shv['one'] = {"eins":1, "zwei":2, "drei":3}
finally:
    shv.close()


shv = shelve.open(r'shv.db')
try:
    one = shv['one']
    print(one)
finally:
    shv.close()


# shelve忘记写回，需要使用强制写回
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] =100
finally:
    shv.close()
    
    
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()



# shelve忘记写回，需要使用强制写回 writeback=True
shv = shelve.open(r'shv.db', writeback=True)
try:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容还是存在于内存中，没有写回数据库
    k1["eins"] =100
finally:
    shv.close()
    
    
shv = shelve.open(r'shv.db')
try:
    k1 = shv['one']
    print(k1)
finally:
    shv.close()


# shelve 使用 with 管理上下文环境

with shelve.open(r'shv.db', writeback=True) as shv:
    k1 = shv['one']
    print(k1)
    # 此时，一旦shelve关闭，则内容写回数据库
    k1['eins'] = 1000

with shelve.open(r'shv.db') as shv:
    print(shv['one'])