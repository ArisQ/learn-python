#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Iterable

d = {'a': 1, 'b': 2, 'c': 3}
print(d)
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

print(isinstance(d, Iterable))
print(isinstance(123, Iterable))
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))

for k, v in enumerate(['a', 'b', 'c']):
    print(k, v)


def findMinAndMax(L):
    if len(L) == 0:
        return (None, None)
    m = L[0]
    M = L[0]
    for v in L:
        if v < m:
            m = v
        if v > M:
            M = v
    return (m, M)


# 测试
if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')
