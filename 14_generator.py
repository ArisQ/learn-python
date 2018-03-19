#!/usr/bin/env python3
# -*- coding: utf-8 -*-

g = (x * x for x in range(10))
print(next(g))

try:
    while True:
        print(next(g))
except StopIteration as e:
    print(e.value)


def triangles():
    ln = [1]
    while True:
        yield ln
        i = 0
        nln = []
        for x in ln:
            nln.append(i + x)
            i = x
        nln.append(1)
        ln = nln


# 方法2
def triangles2():
    ln = [1]
    while True:
        yield ln
        # ln.append(0) # ERROR: 会修改已经yield出的list，改变外部的list
        # ln.insert(0,0) #不能先添加首位在相加
        ln = [x + y for x, y in zip(ln[:len(ln) - 1], ln[1:])]
        ln.append(1)
        ln.insert(0, 1)


# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
results = []
for t in triangles():
    print(t)
    results.append(t)
    n = n + 1
    if n == 10:
        break
if results == [
    [1],
    [1, 1],
    [1, 2, 1],
    [1, 3, 3, 1],
    [1, 4, 6, 4, 1],
    [1, 5, 10, 10, 5, 1],
    [1, 6, 15, 20, 15, 6, 1],
    [1, 7, 21, 35, 35, 21, 7, 1],
    [1, 8, 28, 56, 70, 56, 28, 8, 1],
    [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
]:
    print('测试通过!')
else:
    print('测试失败!')
