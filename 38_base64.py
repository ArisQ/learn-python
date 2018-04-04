#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import base64

print(base64.b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.b64decode(b'abcd++//'))
print(base64.urlsafe_b64encode(b'i\xb7\x1d\xfb\xef\xff'))
print(base64.urlsafe_b64decode(b'abcd--__'))


def safe_base64_decode(s):
    while len(s) % 4 != 0:
        s = s + b'='
    return base64.b64decode(s)


# 测试:
assert b'abcd' == safe_base64_decode(b'YWJjZA=='), safe_base64_decode('YWJjZA==')
assert b'abcd' == safe_base64_decode(b'YWJjZA'), safe_base64_decode('YWJjZA')
print('ok')
