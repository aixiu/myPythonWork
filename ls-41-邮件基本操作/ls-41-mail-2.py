#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

fromAddr = 'shendlax@126.com'
myPass = 'shendlax520'
toAddr = '4815563@qq.com'

ret = True
try:
    # 生成一个邮件对象
    msg = MIMEMultipart()
    msg['Subject'] =  'Sunset'  # 主题
    msg['From'] = fromAddr
    msg['To'] = toAddr
    # msg.preamble = 'When the sun has set, no candle can replace it.'
    body = 'When the sun has set, no candle can replace it.\n\n\n'

    msg.attach(MIMEImage(body, 'plain'))

    with open('sunset.jpg','rb') as fp:
        img = MIMEImage(fp.read())

    msg.attach(img)   # 把读取到的图片添加进去用 attach 

    server = smtplib.SMTP("smtp.126.com", 25)  #设置邮件服务器
    server.starttls()  # TLS服务器启动
    server.login(fromAddr, myPass)  # 添加登录用户邮箱和密码

    server.send_message(msg)  # 发送 msg 对象内的所有内容

    server.quit()  # 关闭服务器
except Exception:
    ret = False

if ret == True:
    print('\n{:=^20}'.format('邮件发送成功'))
else:
    print('\n{:=^20}'.format('邮件发送失败'))