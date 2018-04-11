#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import poplib
from email.parser import Parser
from email.header import decode_header


class EmailAccount:
    def __init__(self, name, addr, passwd, smtp, pop3):
        self.name = name
        self.addr = addr
        self.passwd = passwd
        self.smtp = smtp
        self.pop3 = pop3


sohu_account = EmailAccount(
    name='python_test_sohu',
    addr='python_test_2018@sohu.com',
    passwd='python123456',
    smtp='smtp.sohu.com',
    pop3='pop3.sohu.com')
netease_account = EmailAccount(
    name='python_test_netease',
    addr='python_test_2018@163.com',
    passwd='py123456',
    smtp='smtp.163.com',
    pop3='pop3.163.com')


def guess_charset(msg):
    charset = msg.get_charset()
    if not charset:
        content_type = msg.get('Content-Type', '').lower()
        pos = content_type.find('charset=')
        if pos > 0:
            charset = content_type[pos + 8:].strip()
    return charset


def print_msg(msg, indent=0):
    if indent == 0:
        print('==============================')
        for header in ['From', 'To', 'Subject']:
            v = msg.get(header, '')
            if v:
                hdr = decode_header(v)
                v, charset = hdr[0]
                if charset:
                    v = v.decode(charset)
            print('%s: %s' % (header, v))  # indent==0
    if msg.is_multipart():
        parts = msg.get_payload()
        for part in parts:
            print('%s------------------------------' % ('    ' * indent))
            print_msg(part, indent + 1)
    else:
        content_type = msg.get_content_type()
        if content_type == 'text/plain' or content_type == 'text/html':
            content = msg.get_payload(decode=True)
            charset = guess_charset(msg)
            if charset:
                content = content.decode(charset)
            print('%sText: %s' % ('     ' * indent, content))
        else:
            print('%sAttachment: %s' % (' ' * indent, content_type))


account = netease_account
server = poplib.POP3(account.pop3)
server.set_debuglevel(1)
print(server.getwelcome().decode('utf-8'))
server.user(account.addr)
server.pass_(account.passwd)
print(server.stat())
resp, emails, octets = server.list()
print(resp)
print(emails)
print(octets)
for i in range(len(emails)):
    resp, lines, octets = server.retr(i + 1)  # 从1开始
    msg_content = b'\r\n'.join(lines).decode('utf-8')
    msg = Parser().parsestr(msg_content)
    print_msg(msg)
    server.dele(i + 1)  # 删除邮件
server.quit()
