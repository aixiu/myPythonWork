#!/usr/bin/env python
# -*- coding: utf-8 -*-

# csv 文件操作  读取
import csv
# exampleFile = open('example.csv')
# exampleReader = csv.reader(exampleFile)

# print(exampleReader)

# exampleData = list(exampleReader)
# print(exampleData)
# print(exampleData[0][2])
# print(exampleData[2][1])
# print(exampleData[3][0])

# 用FOR 循环来读取方法
# exampleFile.seek(0)  #  把文件指针，指向最开始
# for row in exampleReader:
#     print('Row #', exampleReader.line_num, row)
# exampleFile.close()   # 关闭文件
# 结论：reader,读对象,只能读一次，指针就到最后，
# 第二次需把指针如0或是新建一个读对象   .seek(0)指针归零。

# csv 文件操作  写入
# outputFile = open('output.csv', 'w')
outputFile = open('output.csv', 'w', newline='') 
# 如果是Windwos: 末尾设置，新行为空。不加的话会行间距会自动加一行。


outputWriter = csv.writer(outputFile)
outputWriter.writerow(['spam', 'eggs', 'bacon', 'ham'])
outputWriter.writerow(['Hello, world!', 'eggs', 'bacon', 'ham'])
outputWriter.writerow([1, 2, 3.1415, 4])
outputFile.close()

# 改变默认的','分割，用自定义的 TAB 分割
# csvFile = open('exapmpl.tsv', 'w')
# csvWriter = csv.writer(csvFile, delimiter='\t', lineterminator='\n\n')
# # 注：delimiter 设置分割符为 TAB，lineterminator设置行与行之间的间距，默认一个换行，现设置两个。
# csvWriter.writerow(['apples', 'oranges', 'grapes'])
# csvWriter.writerow(['eggs', 'bacon', 'ham'])
# csvWriter.writerow(['salad', 'salad', 'salad', 'salad', 'salad'])
# csvFile.close()