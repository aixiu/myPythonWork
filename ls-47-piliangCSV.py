#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 批量处理CSV文件 把文件夹下所有的 CSV 文件拿出来去掉头部
import csv
import shutil  # 对文件，文件夹的复制，删除操作模块
import pathlib

srcPath = './removeCsvHeader/'  # 原始文件夹
destPATH = './headerRemoved/'  # 复制后的文件夹，对复制后的文件处理



