#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


fromAddr = 'shendlax@126.com'
myPass = 'shendlax520'
toAddr = '4815563@qq.com'

ret = True
try:
    msg = MIMEMultipart()
    msg['From'] =  fromAddr
    msg['To'] = toAddr
    msg['Subject'] = 'Narcissistic Cannibal'  # 主题

    body = '''
    Dot't wanna be sly and defile you
    此处是邮件内容
    '''
    msg.attach(MIMEText(body, 'plain')) 

    server = smtplib.SMTP("smtp.126.com", 25)
    server.starttls()
    server.login(fromAddr, myPass)

    text = msg.as_string()   # 方式一： 把 msg 对象的字符串提取出来 用as_string()方式
    server.sendmail(fromAddr, toAddr, text)

    # server.send_message(msg)  # 方式二

    server.quit()
except Exception:
    ret = False

if ret == True:
    print('\n{:=^20}'.format('发送成功'))
else:
    print('\n{:=^20}'.format('发送失败'))


# server = smtplib.SMTP("smtp.126.com", 25)
# server.starttls()
# server.login("shendlax@126.com", "shendlax520")

# msg = 'hello! aixiu'

# server.sendmail('shendlax@126.com', '4815563@qq.com', msg)
# server.quit()