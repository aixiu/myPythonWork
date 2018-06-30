# https://medium.freecodecamp.org/send-emails-using-code-4fcea9df63f
# http://note.youdao.com/noteshare?id=0660be248f8590943ae834fa585ebbc9&sub=D00762271AE4495EAF5D50541F025326
# 一个从TXT文本中提取目标邮箱和邮件内容的关例。

MY_ADDRESS = 'shendlax@126.com'
MY_PASSWORD = 'shendlax520'

# 函数从一个给定的联系人文件中读取联系人并返回
# 姓名和电子邮件地址列表

def get_contacts(filename):
    names = []
    emails = []
    with open(filename, mode='r', encoding='utf-8') as contacts_file:
        for a_contact in contacts_file:
            names.append(a_contact.split()[0])
            emails.append(a_contact.split()[1])
    return names, emails

# 还需要一个函数来读取模板文件（例如message.txt）并返回Template由其内容构成的对象。
from string import Template

def read_template(filename):
    with open(filename, mode='r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)

# 导入模块的smtplib。默认情况下它应该在Python中自带
import smtplib

# 设置 SMTP 服务器
s = smtplib.SMTP_SSL(host='smtp.126.com', port=465)
# outlook: s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
# Gmail: s = smtp.gmail.com: port (TLS):587; port (SSL):465

s.login(MY_ADDRESS, MY_PASSWORD)

# 现在用我们上面定义的功能获取联系信息和消息模板的内容
names, emails = get_contacts('mycontacts.txt')
message_template = read_template('message.txt')

# 开始分别发邮件
# import 必要的包
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ret = True
try:
    # 对于每个联系人，发送电子邮件
    for name, email in zip(names, emails):
        msg = MIMEMultipart()  # 创建一个消息容器

        # 在消息模板中添加实际的人名  中文直接用PERON_NAME = name就行，如果名字为英文，name.title 会把首字母大写
        message = message_template.safe_substitute(PERON_NAME = name.title()) # 字符串模板的安全替换(safe_substitute)

        # 设置消息的参数
        msg['From'] = MY_ADDRESS
        msg['To'] = email
        msg['Subject'] = '美丽的郧西'  # 主题

        # 添加邮件正文主体
        msg.attach(MIMEText(message))
        # 通过之前设置的服务器发送消息。
        s.send_message(msg)

        del msg

    s.quit()

except Exception:
    ret = False

if ret == True:
    print('\n{:=^20}'.format('邮件发送成功'))
else:
    print('\n{:=^20}'.format('邮件发送失败'))