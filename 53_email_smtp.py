#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart, MIMEBase
from email import encoders
from email.header import Header
from email.utils import formataddr
import smtplib


class EmailAccount:
    def __init__(self, name, addr, passwd, smtp, pop3):
        self.name = name
        self.addr = addr
        self.passwd = passwd
        self.smtp = smtp
        self.pop3 = pop3


def send_email(from_account, to_account, subject, msg):
    msg['From'] = formataddr((from_account.name, from_account.addr))
    msg['To'] = formataddr((to_account.name, to_account.addr))
    msg['Subject'] = Header(subject, 'utf-8').encode()
    server = smtplib.SMTP(from_account.smtp, 25)
    server.set_debuglevel(1)
    server.login(from_account.addr, from_account.passwd)
    server.sendmail(from_account.addr, [to_account.addr], msg.as_string())
    server.quit()


sohu_account = EmailAccount(
    name='python_test_sohu',
    addr='python_test_2018@sohu.com',
    passwd='python123456',
    smtp='smtp.sohu.com',
    pop3='pop3.sohu.com')
netease_accout = EmailAccount(
    name='python_test_netease',
    addr='python_test_2018@163.com',
    passwd='py123456',
    smtp='smtp.163.com',
    pop3='pop3.163.com')

msg = MIMEText('Hello, E-mail!', 'plain', 'utf-8')
send_email(sohu_account, netease_accout, 'Hello, E-mail', msg)

msg2_content = r'''
<html>
<body>
<h1>Hello, HTML E-mail</h1>
<p>Send by <a href="http://www.python.org">Python</a></p>
<body>
<html>
'''
msg2 = MIMEText(msg2_content, 'html', 'utf-8')
send_email(sohu_account, netease_accout, 'Hello, HTML E-mail', msg2)  # 可能在垃圾邮件中,163发送失败，被认为是垃圾邮件DT::SPM

msg3_content = r'''
<html>
<body>
<h1>Hello, Attachment</h1>
<p>Send by <a href="http://www.python.org">Python</a></p>
<img src="cid:0"/>
<body>
<html>
'''
msg3 = MIMEMultipart()
msg3.attach(MIMEText(msg3_content, 'html', 'utf-8'))
with open('./46_pillow/lena.jpg', 'rb') as f:
    mime = MIMEBase('image', 'jpg', filename='lena.jpg')
    mime.add_header('Content-Disposition', 'attachment', filename='lena.jpg')
    mime.add_header('Content-ID', '<0>')
    mime.add_header('X-Attachment-Id', '0')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg3.attach(mime)
with open('53_email_smtp.py', 'rb') as f:
    mime = MIMEBase('text', 'py', filename='smtp.py')
    mime.add_header('Content-Disposition', 'attachment', filename='smtp.py')
    mime.add_header('Content-ID', '<1>')
    mime.add_header('X-Attachment-Id', '1')
    mime.set_payload(f.read())
    encoders.encode_base64(mime)
    msg3.attach(mime)
send_email(sohu_account, netease_accout, 'Hello, Attachment', msg3)
