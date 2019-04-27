#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 考试成绩判断
# 成绩由用户输入
# 90以上： 输出优秀
# 80-90： 输出良
# 70-80： 输出中
# 60-70： 输出平
# 60以下： 输出，我没你这撒学僧

score = int(input('请输入成绩，必须是数字'))

if score >= 90:
    print('优秀')
elif score >= 80:
    print('良')
elif score >= 70:
    print('中')
elif score >= 60:
    print('平')
else:
    print('我没你这撒学僧')

# 循环
    # 语法
        # for 变量 in 序列：
            # 语句1
            # 语句1
list_one = [1,2,3,4,5,6,7]

for shuzi in list_one:
    print(shuzi)

# 打印学生列表姓名
# 如果是 jingjing ，那肯定是我的最爱呀。
# 如果是别撑生，那要冷酷的拒绝他

stu_list = ['王大雁','李美丽','王晓静']

for stu in stu_list:
    if stu == '王晓静':
        print('晓静你去哪里了')        
    else:
        print("对不起同学，打扰了")

# for else 语句
    # for 循环结束的时候，有时候需要执行一些收尾工作，皮时需要使用 else 语句。
    # else 语句是可选

stu_list = ['王大雁','李美丽','王晓静']

for stu in stu_list:
    if stu == '王晓静':
        print('晓静你去哪里了')
    else:
        print("对不起同学，打扰了")
else:
    print('不会再爱了')


# break, continue, pass
    # break 无条件结束整个循环，简称循环猝死（当前循环）
    # continue 退出本次循环，继续下次循环
    # pass 只是占位符号,代表这句话啥也不干，没有跳过功能。

# break 案例
    # 确定一个数字队列中是否包含数字7。
    #确定是否包含，只要找到一个即可确定，不需要再继续往下找了，所以使用 break

dig_liat = [3,4,6,7,54,3,23,2,4,7]

for dig in dig_liat:
    if dig == 7:
        print('终于找到你了')
        break
    else:
        print(dig)

# continue 案例
    # 在数字 1-10 中，寻找所有偶数，找到偶数后打印偶数。

dig_list = [1,2,3,4,5,6,7,8,9,10]

for dig in dig_list:
    if dig % 2 == 1:
        continue

    print(dig)
    print('这是偶数')

# pass 案例一

age = 19
if age > 19:
    pass
else:
    print('还小的很呐')

# pass 案例二
ages = [2,23,43,54,65,2]
for age in ages:
    pass
    print(age)

# range 函数
    # 生成有序数列
    # 生成数字队列可以定制

# range 案例1
    # 生成一个从1到100的数字序列
    # range 生成序列的两个数字，是左包，右不包。但是 randint 函数是个特例。

dig_list = range(1,101)
for i in dig_list:
    print(i)

# range 案例2
    # 打印从 1 到 9 的数字
for i in range(1,10):
    print(i)


# while 循环
    # 表示当条件成立时，就循环，适用于不知道具体循环次数，但能确定在某个条件成立时就循环。
    # while语法：

        # while 条件表达式：
        #     语句块

        # 另外一种表达方法

        # while  条件表达式：
        #     语句块1
        # else：
        #     语句块2

