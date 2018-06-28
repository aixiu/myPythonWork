#!/usr/bin/env python
# -*- coding: utf-8 -*-

# https://blog.csdn.net/zl87758539/article/details/53363860
#========================================== 
# 导入smtplib和MIMEText 
from email.mime.text import MIMEText
import smtplib

#========================================== 
# 要发给谁，这里发给2个人 
mailto_list = ['4815563@qq.com', '715209699@qq.com']

#========================================== 
# 设置服务器，用户名、口令
mail_host = 'smtp.126.com'
mail_user = 'shendlax@126.com'
mail_pass = 'shendlax520'

#========================================== 
# 发送邮件

def send_mail(to_list, sub, content):
    '''
    to_list:发给谁 
    sub:主题 
    content:内容 
    send_mail("xxx@xxxx.com","主题","内容") 
    '''

    msg = MIMEText(content)
    msg['Subject'] = sub  # 主题
    msg['From'] =  'shendlax@126.com'
    msg['To'] =  ';'.join(to_list)   # 用字符串‘;’ join 方式，把列表里的元素用该字符串把元素分割

    try:
        s = smtplib.SMTP_SSL(mail_host, 465)
        s.set_debuglevel(0)   # 只是用来打印调试信息的，如果设置为0，就不打印
        s.login(mail_user, mail_pass)
        s.send_message(msg)
        s.close()
        return True

    except Exception as e:
        print(e)
        return False

if __name__ == '__main__':
    if send_mail(mailto_list, '群发邮件标题', '群主邮件内容：测试内容可不可以'):
        print('\n{:=^20}'.format('发送成功'))
    else:
        print('\n{:=^20}'.format('发送失败'))


# if __name__ == '__main__'的意思是：
# 当.py文件被直接运行时，
# if __name__ == '__main__'之下的代码块将被运行；
# 当.py文件以模块形式被导入时，
# if __name__ == '__main__'之下的代码块不被运行。