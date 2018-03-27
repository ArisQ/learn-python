#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def _odd_iter():
    n = 1
    while True:
        n += 2
        yield n


def primes():
    yield 2
    it = _odd_iter()
    while True:
        n = next(it)
        yield n
        it = filter(lambda x: x % n != 0, it)


# 打印1000以内的素数:
for n in primes():
    if n < 1000:
        print(n)
    else:
        break


def is_palindrome(n):
    nl = []
    while n != 0:
        nl.append(n % 10)
        n = n // 10
    return nl[:len(nl) // 2] == nl[-1:-(len(nl) // 2) - 1:-1]


# 测试:
output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))
if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')
