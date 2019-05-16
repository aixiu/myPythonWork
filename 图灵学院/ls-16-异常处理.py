#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 异常
    # 广义上的错误分为错误和异常
    # 错误指的是可以人为避免
    # 异常是指在语法逻辑正确的前提下，出现的问题
    # python 里，异常是一个类，可以处理和使用

# 异常的分类
    # AssertError 断言语句（assert）失败
    # AttributeError 尝试访问未知的对象属性
    # EOFError 用户输入文件末尾标志EOF（Ctrl+d）
    # FloatingPointError 浮点计算错误
    # GeneratorExit generator.close()方法被调用的时候
    # ImportError 导入模块失败的时候
    # IndexError 索引超出序列的范围
    # KeyError 字典中查找一个不存在的关键字
    # KeyboardInterrupt 用户输入中断键（Ctrl+c）
    # MemoryError 内存溢出（可通过删除对象释放内存）
    # NameError 尝试访问一个不存在的变量
    # NotImplementedError 尚未实现的方法
    # OSError 操作系统产生的异常（例如打开一个不存在的文件）
    # OverflowError 数值运算超出最大限制
    # ReferenceError 弱引用（weak reference）试图访问一个已经被垃圾回收机制回收了的对象
    # RuntimeError 一般的运行时错误
    # StopIteration 迭代器没有更多的值
    # SyntaxError Python的语法错误
    # IndentationError 缩进错误
    # TabError Tab和空格混合使用
    # SystemError Python编译器系统错误
    # SystemExit Python编译器进程被关闭
    # TypeError 不同类型间的无效操作
    # UnboundLocalError 访问一个未初始化的本地变量（NameError的子类）
    # UnicodeError Unicode相关的错误（ValueError的子类）
    # UnicodeEncodeError Unicode编码时的错误（UnicodeError的子类）
    # UnicodeDecodeError Unicode解码时的错误（UnicodeError的子类）
    # UnicodeTranslateError Unicode转换时的错误（UnicodeError的子类）
    # ValueError 传入无效的参数
    # ZeroDivisionError 除数为零

l = [1, 2, 3, 4, 5]
# 常范的除零错误
num = int(input('plz input you num:'))
print(100/num)

# 异常处理
    # 不能保证程序永远正确运行
    # 但是，必须保证程序在最坏的情况下得到的问题被妥善得处理
    # python 的异常处理模块全部语法为：
        # try:
        #     尝试实现某个操作，
        #     如果没出现异常，任务就可以完成
        #     如果出现异常，将异常从当前代码块扔出去尝试解决异常

        # except 异常类型1:
        #     解决方案1：用于尝试在此处处理异常解决问题

        # except 异常类型2：
        #     解决方案2：用于尝试在此处处理异常解决问题

        # except (异常类型1,异常类型2...):
        #     解决方案：针对多个异常使用相同的处理方式

        # excpet:
        #     解决方案：所有异常的解决方案

        # else:
        #     如果没有出现任何异常，将会执行此处代码

        #   finally:
        #       管你有没有异常都要执行的代码

# 流程
    # 执行try下面的语句
    # 如果出现异常，则在except语句里查找对应异常病进行处理
    # 如果没有出现异常，则执行else语句内容
    # 最后，不管是否出现异常，都要执行finally语句
    # 除except(最少一个)以外，else和finally可选

# 简单异常安全
try:
    num = int(input('Plz input you nuber:'))
    rst = 100/num
    print('计算结果是: {}'.format(rst))
except:
    print('你输的是什么玩意儿')
    # exit 是退出程序的意思
    exit()


# 简单异常安全
# 给出提示信息
try:
    num = int(input('Plz input you nuber:'))
    rst = 100/num
    print('计算结果是: {}'.format(rst))

# 捕获异常后，把异常实例化，出息信息会在实例里
# 注意以下写法
# 以下语句是捕获ZeroDivisionError异常并实例化实例e
except ZeroDivisionError as e:
    print('你输的是什么玩意儿')
    print(e)
    help(e)
    # exit 是退出程序的意思
    exit()



# 简单异常安全
# 给出提示信息
try:
    num = int(input('Plz input you nuber:'))
    rst = 100/num
    print('计算结果是: {}'.format(rst))

# 如果是多种Error的情况下
# 需要把起越具体的错误，越往前放
# 在异常类继承关系中，越是子类的异常，越要往前放
# 越是父类的导演，越要往后放

# 在处理异常的时候，一旦拦截到开支一个异常，则不在继续往下查看，直接进行下一个
# 代码，即有 finally 则执行 finally语句块，否则就执行下一个大的语句。
except ZeroDivisionError as e:
    print('你输的是什么玩意儿')
    print(e)
    # exit 是退出程序的意思
    exit()
except NameError as e:
    print('名字起错了')
    print(e)

except AttributeError as e:
    print('好像属性有问题')
    print(e)
    exit()

# 所有异常都是继承自 Exception 
# 如果写上下面这句话，任何异常都会拦截住
# 而且，下面这句话一定是最后一个exception
except Exception as e:
    print('我也不知道就出错了')
    print(e)
else:
    print('结束了，这是结果')


# 用户手动引发异常
    # 某些情况，用户希望自己引发一个异常的时企业民，可以使用
    # raise 关键字来引发异常


# raise 案例1
try:
    print('我爱XXX')
    print(3.1415926)

    # 手动引发一个异常
    #　注意写法：　raise ErrorClassName
    raise ValueError
    print('还没写完')
except NameError as e:
    print('NameError')
except ValueError as e:
    print('ValueError')
except Exception as e:
    print('有异常')
finally:
    print('有没有异常我都要执行')


# raise 案例2
# 自己定义异常
# 需要注意： 自定义异常必须是系统异常的子类

class DanaValueError(ValueError):
    pass

try:
    print('我爱XXX')
    print(3.1415926)

    # 手动引发一个异常
    #　注意写法：　raise ErrorClassName
    raise DanaValueError
    print('还没写完')
except NameError as e:
    print('NameError')
except ValueError as e:
    print('ValueError')
except Exception as e:
    print('有异常')
finally:
    print('有没有异常我都要执行')



# else 语句案例
try:
    num = int(input('Plz input you nuber:'))
    rst = 100/num
    print('计算结果是: {}'.format(rst))
except Exception as e:
    print('ExCEPTION')

else:
    print('NO Exception')
finally:
    print('反正我会执行')


# 关于自定义异常
    # 只要是 raise 异常，则推荐自定义异常
    # 在自定义异常的时候，一般包含以下内容：
        # 自定义发生异常的异常代码
        # 自定义发生异常后的问题提示
        # 自定义发生异常的行数
    # 最终的目的是，一旦发生异常，方便程序员快速定位错误现场