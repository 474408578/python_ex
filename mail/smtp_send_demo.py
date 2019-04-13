'''
python使用SMTP协议发送邮件：
    python内置对SMTP支持，可以发送纯文本邮件，HTML邮件，以及带附件的邮件。
    python对SMTP支持有email和smtplib两个模块，email负责构造邮件，smtplib负责发送邮件。
'''

from email.mime.text import MIMEText

# 构造邮件
msg = MIMEText("Hello, send by python...", 'plain', 'utf-8')


# 发送邮件
from_addr = input('From: ')
password = input('Password: ')

to_addr = input('To: ')
smtp_server = input('SMTP server: ')

import smtplib
# 初始化SMTP客户端，默认端口是25
server = smtplib.SMTP(smtp_server, 25)
# 打印出和SMTP服务器交互的所有信息
server.set_debuglevel(1)
# 登录SMTP服务器
server.login(from_addr, password)
# 发送邮件，收件人是list类型， as_string()把MIMEText对象变成str
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()

'''
From: 1*******0@qq.com
Password: *****（开启POP3/SMTP服务或者IMAP/SMTP服务时会生成一个密码，填写哪个密码即可）
To: 1********8@163.com
SMTP server: smtp.qq.com （发送方的MTA）
'''

'''
邮件发送后，有以下问题：
    1、无主题
    2、明明发送到了某个邮箱，收件人列表却是空的。
'''