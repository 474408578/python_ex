'''
在smtp_send_demo.py中、邮件发送后，有以下问题：
    1、无主题
    2、明明发送到了某个邮箱，收件人列表却是空的。

原因：
    邮件主题、如何显示发件人、收件人等信息并不是通过SMTP协议发给MTA，而是包含在发给MTA的文本中的，
    所以，我们必须把From、To和Subject添加到MIMEText中，才是一封完整的邮件：
'''

from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server: ')
subject = input('Subject: ')

msg = MIMEText('hello, send by python...', 'plain', 'utf-8')
msg['From'] = from_addr
msg['To'] = to_addr
msg['Subject'] = Header(subject, 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()





