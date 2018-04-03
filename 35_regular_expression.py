#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import re

print(re.match(r'^\d{3}\-\d{3,8}$', '010-12345'))
print(re.split(r'\s+', 'a b   c'))
m = re.match(r'(\d*):(\d*)', '19:98')
print(m.groups())
print(m.group(0))
print(re.match(r'^(\d+)(0*)$', '10086000').groups())
print(re.match(r'^(\d+?)(0*)$', '10086000').groups())


email_regular = re.compile(r'^[\w\.]+@[\w\.]+$')


def is_valid_email(addr):
    return email_regular.match(addr)


# 测试:
assert is_valid_email('someone@gmail.com')
assert is_valid_email('bill.gates@microsoft.com')
assert not is_valid_email('bob#example.com')
assert not is_valid_email('mr-bob@example.com')
print('ok')


email_name_regular = re.compile(r'^(<([\w\s]+)>)?\s*([\w\.]+)@[\w\.]+$')


def name_of_email(addr):
    print(email_name_regular.match(addr).groups())
    m = email_name_regular.match(addr)
    if not (m.group(2) is None):
        return m.group(2)
    else:
        return m.group(3)


# 测试:
assert name_of_email('<Tom Paris> tom@voyager.org') == 'Tom Paris'
assert name_of_email('tom@voyager.org') == 'tom'
print('ok')
