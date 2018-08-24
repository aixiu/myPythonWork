#!/usr/bin/env python
# -*- coding: utf-8 -*-
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
def mail(user): 
    ret = True
    try:
        msg = MIMEText("自学python，一直在在看武老师的视频，谢谢。", "plain", "utf-8")
        msg["From"] = formataddr(["叶叶菜","shendlax@126.com"])
        msg["To"] = formataddr(["菜菜","4815563@qq.com"])
        msg["Subject"] = "感谢信"
        
        server = smtplib.SMTP("smtp.126.com", 25)
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