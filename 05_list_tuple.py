#!/usr/bin/env python3
# -*- coding: utf-8 -*-

classmates = ['Michael', 'Bob', 'Tracy']
print(classmates)
print(len(classmates))
print(classmates[0])
print(classmates[-1])
classmates.insert(1, 'Jack')
print(classmates)
print(classmates.pop())
print(classmates)
print(classmates.pop(1))
print(classmates)
print(['A', 123, True])

classmates = ('Michael', 'Bob', 'Tracy')
print(len(classmates))
print(classmates[0])
print(classmates[-1])
print(())  # 空tuple
print((1))  # 错误的保护一个元素tuple
print((1,))  # 保护一个元素的tuple
t = (1, 2, [3, 4])
print(t)
t[2][0] = 5
print(t)
