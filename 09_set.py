#!/usr/bin/env python3
# -*- coding: utf-8 -*-

s = set([1, 2, 3])
print(s)
s.add(4)
print(s)
s.remove(4)
print(s)

s1 = set(range(5))
s2 = {3, 4, 5, 6}
s3 = set({'A', 'B', 'C'})
print(s1)
print(s2)
print(s3)
print(s1 & s3)
print(s1 & s2)
print(s1 | s2)
print(s1 - s2)
print(s1 ^ s2)
print({1} < s1)
print(s1 > s2)

st = {(1, 2), (3, 4, 5)}
print(st)
st = {(1, 2), 3, "A"}
print(st)
# st = {(1, 2), [3, 4, 5]}  # TypeError: unhashable type: 'list'
