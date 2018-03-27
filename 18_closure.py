#!/usr/bin/env python3
# -*- coding: utf-8 -*-

fs = []
for i in range(4):
    fs.append(lambda: i * i)
for i in range(4):
    print(fs[i]())


def count():
    fs = []
    for i in range(1, 4):
        fs.append(lambda: i * i)
    return fs


def count2():
    fs = []
    for i in range(1, 4):
        fs.append((lambda x: lambda: x * x)(i))
    return fs


f1, f2, f3 = count()
print(f1())
print(f2())
print(f3())
f1, f2, f3 = count2()
print(f1())
print(f2())
print(f3())


def createCounter():
    x = 0

    def counter():
        nonlocal x
        x += 1
        return x

    return counter


def createCounter2():
    def count_generator():
        x = 0
        while True:
            x += 1
            yield x

    cg = count_generator()

    def counter():
        return next(cg)

    return counter


# 测试:
counterA = createCounter()
print(counterA(), counterA(), counterA(), counterA(), counterA())  # 1 2 3 4 5
counterB = createCounter()
if [counterB(), counterB(), counterB(), counterB()] == [1, 2, 3, 4]:
    print('测试通过!')
else:
    print('测试失败!')
