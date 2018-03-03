#!/usr/bin/env python3
# -*- coding: utf-8 -*-

print("你好，世界！")
print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(25991))
print('\u4e2d\u6587')

print('ABC'.encode('ascii'))
print('中文'.encode('utf-8'))
print(b'ABC'.decode('utf-8'))
print(b'\xe4\xbd\xa0\xe5\xa5\xbd'.decode('utf-8'))

print(len('abc'))
print(len(b'abc'))
print(len('中文字符串'))
print(len('中文字符串'.encode('utf-8')))