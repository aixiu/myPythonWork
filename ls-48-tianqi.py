#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想了解哪个城市的天气状况 功谭，数据转换
import json

stringOfJsonData = '{"name": "Zophie", "isCat": true, "miceCaught": 0, "felingIQ": null}'
jsonDataAsPythonValue = json.loads(stringOfJsonData)
# # json.loads()函数是将json格式数据转换为字典
# # （可以这么理解，json.loads()函数是将字符串转化为字典）
print(type(jsonDataAsPythonValue))
print(jsonDataAsPythonValue)

pythonValue = {'isCat': True, 'miceCaught': 0, 'name': 'Zophie', 'felineIQ': None}
stringOfJsonData = json.dumps(pythonValue)
# json.dumps()函数是将一个Python数据类型列表进行json格式的编码
# （可以这么理解，json.dumps()函数是将字典转化为字符串）
print(type(stringOfJsonData))
print(stringOfJsonData)