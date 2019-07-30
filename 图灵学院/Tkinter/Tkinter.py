#!/usr/bin/env python
# -*- coding: utf-8 -*-


# GUI介绍
    # GraphicalUserInterface,
    # GUI for Python: Tkinter, wxPython, PyQt
    # TKinter:
        # 绑定的是TK GUI工具集，用途Python包装的Tcl代码
    # PyGTK
        # Tkinter的替代品
    # wxPython
        # 跨平台的Python GUI
    # PyQt
        # 跨平台的
        # 商业授权可能有问题


    # 推荐资料
        # 辛星GUI， 辛星Python
        # Python GUI Programming cookbook
        # Tkinter reference a GUI for Python


# 测试tkinter包是否好用
import tkinter

tkinter._test()



# hello world
import tkinter

base = tkinter.Tk()

# 消息循环
base.mainloop()


# Tkinter 常用组件
    # 按钮
        #   Button                按钮组件
        #   RadioButton            单选框组件
        #   CheckButton            选择按钮组件
        #   Listbox                列表框组件

    # 文本输入组件
        #   Entry                单行文本框组件
        #   Text                多行文本框组件

    # 标签组件
        #   Label                标签组件，可以显示图片和文字
        #   Message                标签组件，可以根据内容将文字换行

    # 菜单
        #   Menu                菜单组件
        #   MenuButton            菜单按钮组件，可以使用Menu代替

    # 滚动条
        #   scale                滑块组件
        #   Scrollbar            滚动条组件

    # 其他组件
        #  Canvas                画布组件
        #  Frame                框架组件，将多个组件编组
        #  Toplevel            创建子窗口容器组件
        


# 组件的大致使用步骤
    # 创建总面板
    # 创建面板上的各种组件

        # 指定组件的父组件，即依附关系
        # 利用相应的属性对组件进行设置
        # 给组件安排布局

    # 同步骤2相似，创建好多个组件

    # 最后，启动总面板的消息循环




# Label的例子

import tkinter

base = tkinter.Tk()
# 负责标题
base.wm_title("Label Test")

lb = tkinter.Label(base, text="Python Label")
# 给相应组件指定布局
lb.pack()


base.mainloop()



# 设置Label的例子
import tkinter


base = tkinter.Tk()
base.wm_title("Label Test")
# 支持属性很多background, font, underline等
# 第一个参数，制定所属
lb1= tkinter.Label(base, text="Python AI")
lb1.pack()

lb2= tkinter.Label(base, text="绿色背景", background="green")
lb2.pack()

lb3= tkinter.Label(base, text="蓝色背景", background="blue")
lb3.pack()

base.mainloop()





# Button的案例

import tkinter

def showLabel():
    global baseFrame
    # 在函数中定义了一个label
    # label的父组件是baseFrame
    lb = tkinter.Label(baseFrame, text="显示Label")
    lb.pack()


baseFrame = tkinter.Tk()
# 生成一个按钮
# command参数指示，当按钮被按下的时候，执行哪个函数
btn = tkinter.Button(baseFrame, text="Show Label", command=showLabel)
#btn = tkinter.Button(baseFrame, text="Show Label")
btn.pack()

baseFrame.mainloop()

'''
Button的属性：

anchor 				设置按钮中文字的对其方式，相对于按钮的中心位置
background(bg) 		设置按钮的背景颜色
foreground(fg)		设置按钮的前景色（文字的颜色）
borderwidth(bd)		设置按钮边框宽度
cursor				设置鼠标在按钮上的样式
command				设定按钮点击时触发的函数
bitmap				设置按钮上显示的位图
font				设置按钮上文本的字体
width				设置按钮的宽度  (字符个数)
height				设置按钮的高度  (字符个数)
state				设置按钮的状态
text				设置按钮上的文字
image				设置按钮上的图片

'''




# 组件布局
    # 控制组件的摆放方式
    # 三种布局：

        # pack: 按照方位布局
        # place: 按照坐标布局
        # grid： 网格布局


    # pack布局

        # 最简单，代码量最少，挨个摆放，默认从上倒下，系统自动设置
        # 通用使用方式为： 组件对象.pack(设置，，，，，，，）
        # side: 停靠方位， 可选值为LEFT,TOP,RIGHT,BOTTON
        # fill: 填充方式,X,Y,BOTH,NONE
        # expande: YES/NO
        # anchor: N,E,S,W,CENTER
        # ipadx: x方向的内边距
        # ipady: y
        # padx: x方向外边界
        # pady： y........


    # grid布局

        # 通用使用方式：组件对象.grid(设置,,,,,,,)
        # 利用row，column编号，都是从0开始
        # sticky： N,E,S,W表示上下左右，用来决定组件从哪个方向开始
        # 支持ipadx，padx等参数，跟pack函数含义一样
        # 支持rowspan，columnspan，表示跨行，跨列数量


    # place布局

        # 明确方位的摆放
        # 相对位置布局，随意改变窗口大小会导致混乱
        # 使用place函数，分为绝对布局和相对布局，绝对布局使用x，y参数
        # 相对布局使用relx，rely, relheight, relwidth



# pack布局案例
import tkinter

baseFrame = tkinter.Tk()
# 以下所有代码都是创建一个组件，然后布局

btn1 = tkinter.Button(baseFrame, text='A')
btn1.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='B')
btn2.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame, text='C')
btn2.pack(side=tkinter.RIGHT, expand=tkinter.YES, fill=tkinter.NONE, 
          anchor=tkinter.NE)

btn2 = tkinter.Button(baseFrame, text='D')
btn2.pack(side=tkinter.LEFT, expand=tkinter.NO, fill=tkinter.Y)

btn2 = tkinter.Button(baseFrame, text='E')
btn2.pack(side=tkinter.TOP, expand=tkinter.NO, fill=tkinter.BOTH)

btn2 = tkinter.Button(baseFrame, text='F')
btn2.pack(side=tkinter.BOTTOM, expand=tkinter.YES)

btn2 = tkinter.Button(baseFrame, text='G')
btn2.pack(anchor=tkinter.SE)



baseFrame.mainloop()






# grid布局案例
import tkinter

baseFrame = tkinter.Tk()

#下面被注释掉的一行代码跟下面两行代码等效
#lb1 = tkinter.Label(baseFrame, text="账号: ").grid(row=0, sticky= tkinter.W)
lb1 = tkinter.Label(baseFrame, text="账号: ")
lb1.grid(row=0, sticky= tkinter.W)

en = tkinter.Entry(baseFrame)
en.grid(row=0, column=1, sticky=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码: ").grid(row=1, sticky= tkinter.W)
tkinter.Entry(baseFrame).grid(row=1, column=1, sticky=tkinter.E)

btn = tkinter.Button(baseFrame, text="登录").grid(row=2, column=1, sticky=tkinter.W)


baseFrame.mainloop()




# 消息机制
    # 消息的传递机制
        # 自动发出事件/消息
        # 消息有系统负责发送到队列
        # 由相关组件进行绑定/设置
        # 后端自动选择感兴趣的事件并做出相应反应
    # 消息格式：
        # <[modifier-]---type-[-detail]>
        # <Button-1>: Button表示一个按钮事件，1代表的是鼠标左键，2代表中键



# 事件的简单例子
import tkinter

def baseLabel(event):
        global  baseFrame
        print("哈哈，我被点击了")
        lb = tkinter.Label(baseFrame, text="谢谢点击")
        lb.pack()

# 画出程序的总框架
baseFrame = tkinter.Tk()

lb = tkinter.Label(baseFrame, text="模拟按钮")
# label绑定相应的消息和处理函数
# 自动获取左键点击，并启动相应的处理函数baseLabel
lb.bind("<Button-1>", baseLabel)
lb.pack()

# 启动消息循环
# 到此，表示程序开始运行
baseFrame.mainloop()



# Tkinter的绑定
    # bind_all: 全局范围的绑定，默认的是全局快捷键，比如F1是帮助文档
    # bind_class: 接受三个参数，第一个是类名，第二个是事件，第三个是操作
    # w.bind_class("Entry", "
    # bind:单独对某一个实例绑定
    # unbind： 解绑，需要一个参数，即你要解绑哪个事件

# Entry
    # 输入框，功能单一
    # entry["show"] = "*", 设置遮挡字符






# 输入框案例

import tkinter

# 模拟的是登录函数
def reg():
    # 从相应输入框中，得到用户的输入
    name = e1.get()
    pwd = e2.get()

    t1 = len(name)
    t2 = len(pwd)

    if name == "111" and pwd == "222":
        # 需要理解下面代码的含义
        lb3["text"] = "登录成功"
    else:
        lb3['text'] = "用户名或密码错误"
        # 输入框删除掉用户输入的内容
        # 注意delete的两个参数，表示从第几个删除到第几个
        e1.delete(0,t1)
        e2.delete(0,t2)
        
# 启动舞台
baseFrame = tkinter.Tk()

lb1 = tkinter.Label(baseFrame, text="用户名")
lb1.grid(row=0, column=0, stick=tkinter.W )

e1 = tkinter.Entry(baseFrame)
e1.grid(row=0, column=1, stick=tkinter.E)

lb2 = tkinter.Label(baseFrame, text="密码: ")
lb2.grid(row=1, column=0, stick=tkinter.W )

e2 = tkinter.Entry(baseFrame)
e2.grid(row=1, column=1, stick=tkinter.E)
e2['show'] = '*'

# Button参数command的意思是，当按钮被点击后启动相应的处理函数
btn = tkinter.Button(baseFrame, text="登录", command=reg)
btn.grid(row=2, column=1, stick=tkinter.E)

lb3 = tkinter.Label(baseFrame, text="")
lb3.grid(row = 3)

# 启动主Frame
baseFrame.mainloop()




# 菜单
    # 1. 普通菜单
    # 第一个Menu类定义的是parent
    # add_command 添加菜单项，如果菜单是顶层菜单，则从左向右添加，否则就是下拉菜单
        # label： 指定菜单项名称
        # command: 点击后相应的调用函数
        # acceletor： 快捷键
        # underline： 制定是否菜单信息下有横线
        # menu：属性制定使用哪一个作为顶级菜单




# 普通菜单的代码
import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

for item in ['File', 'Edit', 'View', 'About']:
    menubar.add_command(label=item)

baseFrame['menu'] = menubar

baseFrame.mainloop()





# 级联菜单
    # add_cascade:级联菜单，作用是引出后面的菜单
    # add_cascade的menu属性：指明把菜单级联到哪个菜单上
    # label： 名称
    # 过程：
        # 建立menu实例
        # add_command
        # add_cascade



import tkinter

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)

emenu = tkinter.Menu(menubar)
for item in ['Copy', 'Past', 'Cut']:
    emenu.add_command(label=item)

menubar.add_cascade(label='File')
menubar.add_cascade(label='Edit', menu=emenu)
menubar.add_cascade(label='About')

baseFrame['menu'] = menubar

baseFrame.mainloop()




# 弹出式菜单
    # 弹出菜单也叫上下文菜单
    # 实现的大致思路
        # 简理财单并向菜单添加各种功能
        # 监听鼠标右键
        # 如果右键点击，则根据位置判断弹出
        # 调用Menu的pop方法
    # add_separator: 添加分隔符


import tkinter

def makeLabel():
    global baseFrame
    tkinter.Label(baseFrame, text="PHP是最好的编程语言，我用Python").pack()

baseFrame = tkinter.Tk()

menubar = tkinter.Menu(baseFrame)
for x in ['麻辣香菇', '气锅鸡', '东坡肘子']:
    menubar.add_separator()
    menubar.add_command(label=x)
    
menubar.add_command(label='重庆火锅', command=makeLabel)

# 事件处理函数一定要至少有一个参数，且第一个参数表示的是系统事件
def pop(event):
    # 注意使用 event.x 和 event.x_root的区别 
    #menubar.post(event.x_root, event.y_root)
    menubar.post(event.x_root, event.y_root)

baseFrame.bind("<Button-3>", pop)

baseFrame.mainloop()




# canvas 画布
    # 画布： 可以自由的在上面绘制图形的一个小舞台
    # 在画布上绘制对象， 通常用create_xxxx，xxxx=对象类型， 例如line，rectangle
    # 画布的作用是把一定组件画到画布上显示出来
    # 画布所支持的组件：
        # arc
        # bitmap
        # image(BitmapImage, PhotoImage)
        # line
        # oval
        # polygon
        # rectangle
        # text
        # winodw（组件）
    # 每次调用create_xxx都会返回一个创建的组件的ID，同时也可以用tag属性指定其标签
    # 通过调用canvas.move实现一个一次性动作



    
# 简单画布
import tkinter

baseFrame = tkinter.Tk()

cvs = tkinter.Canvas(baseFrame, width=300, height=200)
cvs.pack()

# 一条线需要两个点指明起始
# 参数数字的单位是px
cvs.create_line(23,23, 190,234)
cvs.create_text(56,67, text="I LOVE PYTHON")


baseFrame.mainloop()




# 画一个五角星
import tkinter
import math as m

baseFrame = tkinter.Tk()

w = tkinter.Canvas(baseFrame, width=300, height=300, background="gray" )
w.pack()


center_x = 150
center_y = 150

r = 150

# 依次存放五个点的位置
points = [
        #左上点
        # pi是一个常量数字，3.1415926
        center_x - int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),

        #右上点
        center_x + int(r * m.sin(2 * m.pi / 5)),
        center_y - int(r * m.cos(2 * m.pi / 5)),

        #左下点
        center_x - int(r * m.sin( m.pi / 5)),
        center_y + int(r * m.cos( m.pi / 5)),

        #顶点
        center_x,
        center_y - r,

        #右下点
        center_x + int(r * m.sin(m.pi / 5)),
        center_y + int(r * m.cos(m.pi / 5)),
    ]

# 创建一个多边形
w.create_polygon(points, outline="green", fill="yellow")
w.create_text(150,150, text="五角星")

baseFrame.mainloop()










import tkinter

baseFrame = tkinter.Tk()

def btnClick(event):
        global  w
        w.move(id_ball, 12,5)
        w.move("fall", 0,5)



w = tkinter.Canvas(baseFrame, width=500, height=400)
w.pack()
w.bind("<Button-1>", btnClick)

# 创建组件后返回id
id_ball  = w.create_oval(20,20, 50,50, fill="green")

# 创建组件使用tag属性
w.create_text(123,56, fill="red", text="ILovePython", tag="fall")
# 创建的时候如果没有指定tag可以利用addtag_withtag添加
# 同类函数还有 addtag_all, addtag_above, addtag_xxx等等
id_rectangle = w.create_rectangle(56,78,173,110, fill="gray")
w.addtag_withtag("fall", id_rectangle)


baseFrame.mainloop()