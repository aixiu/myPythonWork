#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 定义一个类，有下面的类属性

# 1、姓名
# 2、年龄
# 3、成绩（语文， 数学， 英语）每课成绩类型为整数类方法。
# 4、获取学生的姓名：get_name() 返回类型：str
# 5、获取学生的年纪：get_age() 返回类型：int
# 6、返回3们科目中最高的分数，get_course()返回类型：int

class Student(object):
    def __init__(self, name, age, scorse):
        self.name = name
        self.age =  age
        self.scorse = scorse

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def get_course(self):
        return max(self.scorse)

mm =Student('量子', 28, [80, 100, 90])

print(mm.get_name())
print(mm.get_age())
print(mm.get_course())


# 定义一个字典类： DictClass,完成如下功能
# 1、删除某个 key del_dict(key)
# 2、判断某个键是否存字典蠕 ，如果在返回键对应的值，如果不在则返回 not found get_dict()
# 3、返回键组成的列表  返回类型：list get_key()
# 4、合并字典，并且返回合并后字典的 values 组成的列表，返回类型 list update_dict()

class DictClass(object):
    
    def __init__(self, dict):
        self.dict = dict

    def del_dict(self, key):
        #判断 key 是否在字典里
        if key not in self.dict.keys():
            return '你所操作的 kye 不在字典里'
        else:
            sefl.dict.pop(key)
            return '删除成功'

    def get_dict(self, key):
        if key not in self.dict.keys():
            return 'not found'
        else:
            return self.dict[key]

    def get_key(self):
        return self.dict.keys()

    def update_dict(self, dict2):
        self.dict = dict(self.dict, **dict2)
        return self.dict.values()


dd = DictClass({'a':11, 'b':22})

print(dd.update_dict({'c':33}))
