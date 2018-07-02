#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 你想了解哪个城市的天气状况 功谭，数据转换
import json
import datetime
import requests

APP_KEY = 'e622d6be9d063442d07ce2faed795e85'   # Obtain your from : https://openweathermap.org/

def time_converter(time):  # 时间转换函数，把Unix时间转换成我们需要的时间。
    converted_time = datetime.datetime.fromtimestamp(
        int(time)
    ).strftime('%I:%M %p')  # .fromtimestamp 获取时间戳，转换成字符串日期时间 .strftime 定义时间格式
    return converted_time

def url_builder_name(city_name):
    unit = 'metric'  # 设置成摄氏度
    api = 'api.openweathermap.org/data/2.5/weather?q='
    api.map.baidu.com/telematics/v3/weather?location=十堰&output=json&ak=QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT
    full_api_url = api + city_name  + '&units=' + unit + '&APPID=' + APP_KEY
    return full_api_url

def data_fetch(full_api_url):
    response = requests.get(full_api_url)
    try:
        response.raise_for_status()
    except Exception as exc:
        print('There was a problem: {}'.format(exc))
    
    return json.loads(response.text)

def data_organizer(raw_data):
    main = raw_data.get('main')
    sys = raw_data.get('sys')
    data = {
        'city': raw_data.get('name'),
        'country': sys.get('country'),
        'temp': main.get('temp'),
        'temp_max': main.get('temp_max'),
        'temp_min': main.get('temp_min'),
        'humidity': main.get('humidity'),
        'pressure': main.get('pressure'),
        'sky': raw_data['weather'][0]['main'],
        'sunrise': time_converter(sys.get('sunrise')),
        'sunset': time_converter(sys.get('sunset')),
        'wind': raw_data.get('wind').get('speed'),
        'wind_deg': raw_data.get('deg'),
        'dt': time_converter(raw_data.get(dt)),
        'cloudiness': raw_data.get('clouds').get('all'),
        'description': raw_data['weather'][0]['description']
    }

def data_output(data):
    # ℃
    data['m_symbol'] = '\u00b0' + 'C'   # 为 data 数据添加一个键值摄氏度℃

    s = '''
-----------------------------------------------
    Current weather in: {city}, {country}:
    {temp}{m_symbol} {sky}
    Max: {temp_max}, Min: {temp_min}

    Wind Speed: {wind}, Degree: {wind_deg}
    Humidity: {humidity}
    Cloud: {cloudiness}
    Pressure: {pressure}
    Sunrise at: {sunrise}
    Sunset at: {sunset}
    Description: {description}

    Last update from the server: {dt}
-----------------------------------------------'''
    print(s.format(**data))
# 输出数据为字典型的时候，可以直接用{city}占位，最后打印时用 s.format(**data) 方式，两个**



city = input('Which city you want to check? ')

url = url_builder_name(city)   # 根据API要求建立URL
print(url)
rawData = data_fetch(url)    # 把该链接数据抓去下来
prettyData = data_organizer(rawData)  # 只取出我们取要的数据
data_output(prettyData)  # 输出数据

