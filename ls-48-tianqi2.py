#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想了解哪个城市的天气状况 功谭，数据转换
import json
import datetime
import requests

AK = 'QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT'   # Obtain your from : https://openweathermap.org/

def time_converter(time):  # 时间转换函数，把Unix时间转换成我们需要的时间。
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')  # .fromtimestamp 获取时间戳，转换成字符串日期时间 .strftime 定义时间格式
    return converted_time

def url_builder_name(city_name):
    unit = 'metric'  # 设置成摄氏度
    api = 'api.map.baidu.com/telematics/v3/weather?location='    
    full_api_url = api + city_name  + '&output=json' + '&ak=' + AK
    return full_api_url

def data_fetch(full_api_url):
    response = requests.get(full_api_url)        
    return json.loads(response.text)

error_code=response['error']
    #如果取出的error为0，表示数据正常，否则没有查询到天气信息

    #从字典中取出数据
    results=response['results']
    #根据索引取出城市天气信息字典
    info_dict=results[0]
    #根据字典的key 取出城市名称
    city_name=info_dict['currentCity']
    pm25=info_dict['pm25']
    print('当前城市:%s pm值:%s'%(city_name,pm25))
    #取出天气信息列表
    weather_data=info_dict['weather_data']
    #for循环取出每一天天气的小字典
    for weather_dict in weather_data:
        #取出日期、天气、风级、温度
        date=weather_dict['date']
        weather=weather_dict['weather']
        wind=weather_dict['wind']
        temperature=weather_dict['temperature']
        print('%s %s %s %s'%(date,weather,wind,temperature))







city = input('Which city you want to check? ')

url = url_builder_name(city)   # 根据API要求建立URL
print(url)
# rawData = data_fetch(url)    
# prettyData = data_organizer(rawData)  # 只取出我们取要的数据
# data_output(prettyData)  # 输出数据

