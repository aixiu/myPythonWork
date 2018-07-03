# -*- coding:UTF-8 -*-
import urllib.parse
import urllib.request
import ssl
import json

ssl._create_default_https_context = ssl._create_unverified_context  # 支持HTTPS
key_info = {
            'date': '日期',
            'sunrise': '日出',
            'high': '高温',
            'low': '低温',
            'sunset': '日落',
            'aqi': '空气质量指数',
            'fx': '风向',
            'fl': '风力',
            'type': '类型',
            'notice': '建议'
}

city = str(input('你想查询天气的城市：'))
url = 'https://www.sojson.com/open/api/weather/json.shtml?city='    # 申明URL字符串
url += urllib.parse.quote(city)                                     # 对城市名编码并加入URL

req = urllib.request.urlopen(url)
info = json.loads(req.read())
if info.get('status') == 200:
    weather = info['data']
    # 部分城市PM2.5、PM10值为None，weather['pm25']报错
    today_weather = '湿度：{0}，PM2.5：{1}，PM10：{2}，空气质量：{3}，温度：{4}'.format(weather.get('shidu'), weather.get('pm25'), weather.get('pm10'), weather.get('quality'), weather.get('wendu'))

    print(info['city'] + ' 今日天气：')                              # 打印今日天气
    print(today_weather)
    print("=====================================================")
    print(info['city'] + ' 昨日天气：')                              # 打印昨日天气
    for key in weather['yesterday']:
        print(key_info[key] + ':' + str(weather['yesterday'][key]))
    print("=====================================================")
    print(info['city'] + ' 未来5天气：')                             # 打印未来5天天气
    for i in range(4):
        for key in weather['forecast'][i]:
            print(key_info[key] + ':' + str(weather['forecast'][i][key]))
        print("=====================================================")
else:
    print(info.get('message'))

