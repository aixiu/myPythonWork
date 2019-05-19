#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 创建北京和成都两个校区

    # 创建 Linux\Python 两个课程
    # 创建北京校区的 Python 3期课程和成都校区的 Linux 1期课程
    # 管理员创建了北京校区的学员小张，并将其分配在了python 3期
    # 管理员创建了讲师小周，并将其分配给了Python 3期
    # 讲师小周创建了一条 Python 3期的上课记录 Day02
    # 讲师小周为 Day02 这节课所有的学员批改了作业，小张得了A，小王得了B
    # 学员张查看了自己所报的课程
    # 学员小张在查看了自己在Python 3期的成绩列表然后退出了
    # 学员小张给了讲师小周好评

class School(object):
    def __init__(self, school_name)