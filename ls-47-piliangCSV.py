#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 批量处理CSV文件 把文件夹下所有的 CSV 文件拿出来去掉头部
import csv
import shutil  # 对文件，文件夹的复制，删除操作模块
import pathlib

srcPath = './removeCsvHeader/'  # 原始文件夹
destPATH = './headerRemoved/'  # 复制后的文件夹，对复制后的文件处理

# 生成path对象
withHeaderPath = pathlib.Path(srcPath)
withoutHeaderPath = pathlib.Path(destPATH)

# 复制文件夹过程
if not withoutHeaderPath.exists():  # .exists()方法用于检验文件是否存在
    shutil.copytree(srcPath, destPATH)
    # 如果文件夹不存在，用shutil.copytree方法复制一个，连文件夹带文件的目录
    # shutil.copytree()方法，只能用字符串，所以用不能用下边的pash对象
else:
    for f in [x for x in withHeaderPath.iterdir() if x.is_file]:
        # .iterdir()返回一个迭代器, 包含withHeaderPath下所有文件/目录   .is_file检查是否是文件
        shutil.copy(str(f), destPATH)
        # shutil.copy()方法，只能用字符串，所以用str()把 f  转成字符串

# 对复制后的文件夹进行操作，源文件夹不动
for csvFilename in withoutHeaderPath.iterdir():
    if not csvFilename.name.endswith('.csv'):
        # 如果文件名不是.csv结尾
        continue  # 跳过不是.csv文件的处理
    print('Removing headr from >>> ' + str(csvFilename) + ' ...' )  # 显示文件名+ 路径
    # str(csvFilename) 可以获取文件路径+文件名  csvFilename.name 只能获取文件名
    # print('Removing headr from >>> ' + csvFilename.name + ' ...' )  # 只显示文件名

    #去掉文件头，第一行内容,只要第二行以后的内容
    csvRows = []  # 用来储存第二行以后的内容
    csvFileObj = open(csvFilename, 'r')  # 打开文件，并建立对象
    readerOjb = csv.reader(csvFileObj)   # 把文件对象读取，建立读取对象
    for row in readerOjb:
        if readerOjb.line_num == 1:
            continue   # 跳过文件第一行
        csvRows.append(row)   # 把从第二行开始读到的内容，append 到csvRows里，读对象每一行内容就是一个列表
    csvFileObj.close() # 关闭文件对象

    # 开始写文件
    csvFileObj = open(csvFilename, 'w', newline='') # 打开文件，并建立对象
    # 如果是Windwos: 末尾设置，新行为空。不加的话会行间距会自动加一行。

    csvWriter = csv.writer(csvFileObj) # 建立写对象
    for row in csvRows:   # 遍历上边去掉第一行的 csvRows 内容
        csvWriter.writerow(row)  # 写入处理掉第一行的内容 直接在原文件替换掉新内容
    csvFileObj.close()