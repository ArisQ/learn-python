#!/usr/bin/env python3
# -*- coding: utf-8 -*-

L = list(range(20))
print(L)
print(L[:2])
print(L[1:3])
print(L[-1])
print(L[-1:-3])
print(L[-3:-1])
print(L[-3:0])
print(L[-3:])

print(L[1:6:2])
print(L[::3])


def trim(s):
    l = len(s)
    b = 0
    while b < l and s[b] == ' ':
        b += 1
    e = -1
    while e > b - l and s[e] == ' ':
        e -= 1
    return str(s[b:e + l + 1])  # 左闭右开区间


# 测试:
if trim('hello  ') != 'hello':
    print('测试1失败!')
elif trim('  hello') != 'hello':
    print('测试2失败!')
elif trim('  hello  ') != 'hello':
    print('测试3失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试4失败!')
elif trim('') != '':
    print('测试5失败!')
elif trim('    ') != '':
    print('测试6失败!')
else:
    print('测试成功!')
