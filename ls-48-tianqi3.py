#天气预报
# url 统一资源定位符
#windows+r cmd 打开命令  输入pip install requests 回车
#api.map.baidu.com(百度服务器地址)
import requests
#引入python中内置的包
import json
while 1:
    print('*************欢迎进入天气查询系统**************')
    city=input('请输入您要查询的城市名称(按0退出)：')
    if city=='0':
        print('您已退出天气查询系统！')
        break
    else:
        url='http://api.map.baidu.com/telematics/v3/weather?location=%s&output=json&ak=QQBpztQ8fBgON2nn3Qlrj5keExtg7dXT&callback=?'%city
        #使用requests发送请求，接受返回的结果
        response=requests.get(url)
        # print(type(response.text))
        #使用loads函数，将json字符串转换为python的字典或列表
        rs_dict=json.loads(response.text)
        #取出error
        error_code=rs_dict['error']
        #如果取出的error为0，表示数据正常，否则没有查询到天气信息
        if error_code==0:
            #从字典中取出数据
            results=rs_dict['results']
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
        else:
            print('没有查询到天气信息！')
