#!/usr/bin/env python
# -*- coding: utf-8 -*-


import smtplib
from email.mime.text import MIMEText
# from email.utils import formataddr

# MIMEText三个主要参数
    # 1、 邮件内容
    # 2、 MIME子类型，在此案例我们用 plain 表示 text 类型（subtpye）
    # 3、 邮件编码格式

msg = MIMEText('Hello, i am beijing tulingxueyuan', 'plain', 'utf-8')

#  发送 email 地址，此处直接使用QQ邮箱，密码一盘城雕 要临时输入
from_addr = 'shendlax@126.com'

# 引处密码是经过申请设置后的授权码，不是QQ邮箱密码
from_pwd = 'shendlax520xy3'

# 收件人信息
# 此处使用QQ邮箱，给自己发送
to_addr = '4815563@qq.com'

# 输入SMTP服务器地址
# 此处根据不同的邮件服务商，有不同的值
# 现在基本任何一家邮件服务商，如果彩用第三方收发邮件，都需要开启授权选项
# 腾讯QQ邮箱SMTP地址是：smtp.qq.com

smtp_srv = 'smtp.qq.com'

try:
    #两个参数
    # 第一个是服务器地址，但一定是bytes格式，所以需要编码
    # 第二个参数是服务器接受访问的端口
    srv = smtplib.SMTP_SSL(smtp_srv.encode(), 465) # SMTP协议默认端口25

    # 登录邮箱发送
    srv.login(from_addr, from_pwd)

    # 发送邮件
    # 三个参数
    # 1、发送邮件
    # 2、接收地址，必须是 list 形式
    # 3、发送内容，作为字符串发送

    srv.sendmail(from_addr, [to_addr], msg.as_string())

    srv.quit()

except Exception as e:
    print(e)

print('==============案例分割线==============')



def mail(user): 
    ret = True
    try:
        msg = MIMEText("自学python，一直在在看武老师的视频，谢谢。", "plain", "utf-8")
        # MIME子类型，此案例我们用 plain 表示，text类型
        msg["From"] = formataddr(["叶叶菜","shendlax@126.com"])
        msg["To"] = formataddr(["菜菜","4815563@qq.com"])
        msg["Subject"] = "感谢信"
        
        server = smtplib.SMTP("smtp.126.com", 25)      # smtplib.SMTP 老试的，不安全的协议
        server.login("shendlax@126.com", "shendlax520")
        server.sendmail("shendlax@126.com", [user], msg.as_string())
        server.quit()
    except Exception:
        ret = False


    return ret

ret = mail("4815563@qq.com")
if ret == True:
    print("发送成功")
else:
    print("发送失败")