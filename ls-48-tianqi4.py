#!/usr/bin/env python
# -*- coding: utf-8 -*-

#天气预报
#如未安装requests包请用：windows+r cmd 打开命令  输入pip install requests 回车
import json
import requests

AK = 'QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT'   # Obtain your from : api.map.baidu.com

def url_name(city_name):
    api = 'http://api.map.baidu.com/telematics/v3/weather?location='
    # api例子  'http://api.map.baidu.com/telematics/v3/weather?location=城市名字&output=json&ak=QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT'
    full_url = api + city_name + '&output=json' + '&ak=' + AK
    return full_url
    

while True:
    print('\n{:=^40}'.format('欢迎进入天气查询系统'))
    city = input('请输入您要查询的城市名称 / (按 Q 退出)：').upper()
    if city == 'Q':
        print('您已退出天气查询系统！')
        break
    else:
        url = url_name(city)
        # print(url)
        response = requests.get(url)
        # 返回URL包含服务器资源的Response对象 构造一个向服务器请求

        # print(response.status_code)    # 获取返回状态 返回200属正常
        # print(type(response.text))   # response.text数据类型为<class 'str'>

        #使用loads函数，将json字符串转换为python的字典或列表
        rs_dict = json.loads(response.text)

        # 测试用，打印出字天气信息字典方便查看
        # print(rs_dict)

        #取出error
        error_code=rs_dict['error']
        #如果取出的error为0，表示数据正常，否则没有查询到天气信息

        if error_code == 0:
            results = rs_dict['results']
            #从天气信息字典中取出results数据
            city_name = results[0]['currentCity']
            pm25 = results[0]['pm25']
            print('当前城市>>> {}   pm25值>>> {}'.format(city_name, pm25))

            #取出天气信息
            weather_data = results[0]["weather_data"]

            #for循环取出每一天天气的小字典
            for weather_dict in weather_data:
                #取出日期、天气、风级、温度
                date=weather_dict['date']
                weather=weather_dict['weather']
                wind=weather_dict['wind']
                temperature=weather_dict['temperature']
                print('{0} | {1} | {2} | {3}'.format(date, weather, wind, temperature))
        else:
            print('没有查询到 {} 的天气信息！'.format(city))