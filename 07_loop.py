#!/usr/bin/env python3
# -*- coding: utf-8 -*-

for x in range(5):
    print(x)

sum_n = 0
n = 5
for x in list(range(n)):
    sum_n += x
print("sum of 0 ~ %d is %d" % (n - 1, sum_n))

print(range(5))
print(list(range(5)))

sum_n = 0
n = 1000
while n > 0:
    sum_n += n
    n -= 1
print("sum of 0 ~ %d is %d" % (n - 1, sum_n))
