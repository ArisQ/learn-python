#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

print(abs(12.34))
print(abs(-20))

print(min(1, 2))
print(max(1, 2, 5, -1))

print(int('123'))
print(int(12.34))
print(float('123.45'))
print(str(123))
print(bool(123))
print(bool(''))

ABS = abs
print(ABS(-1))

print(hex(-100))


# 函数定义
def factorial(n):
    if not isinstance(n, int):
        raise TypeError('bad operand type')
    if n < 0:
        raise ValueError('negative operand')
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)


for n in range(5):
    print('factorial (%d) = %d' % (n, factorial(n)))


# 空函数
def nop():
    pass


# 求解二次多项式
def quadratic(a, b, c):
    delta = math.sqrt(b * b - 4 * a * c)
    return (-b - delta) / (2 * a), (-b + delta) / (2 * a)


print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-1.0, -0.5):
    print('测试失败')
elif quadratic(1, 3, -4) != (-4.0, 1.0):
    print('测试失败')
else:
    print('测试成功')


# 默认参数
def power(x, n=2):
    if not isinstance(n, int):
        raise TypeError('bad operand type')
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    p = 1
    while n > 0:
        p = p * x
        n -= 1
    return p


print(power(3))
print(power(3, 3))
print(power(3, n=5))  # 传入参数名


# 默认参数必须指向不变对象
def add_end(L=[]):
    L.append('END')
    return L


print(add_end([1, 2, 3]))
print(add_end())
print(add_end())
print(add_end())


# 可变参数
def n_power(*numbers):
    p = []
    for i in numbers:
        p.append(i * i)
    return p


print(n_power())
print(n_power(1, 2, 3))
print(n_power(*[1, 3, 5]))  # list/tuple当可变参数传递


# 关键字参数
def person(name, age, **kw):
    print(name, age, kw)


person('Michael', 30)
person('Bob', 35, city='Beijing')
person('Bob', 35, city='Beijing', country='China')
person('Bob', 35, **{'city': 'Shanghai', 'country': 'China'})


# 命名关键字参数
def person_city_job(name, age, *, city, job='Engineer'):
    print('named parameter:', name, age, city, job)


def person_city_job2(name, age, *args, city, job):
    print('named parameter:', name, age, args, city, job)


person_city_job('Bob', 35, city='Beijing', job='Artist')
person_city_job('Bob', 35, city='Beijing')
person_city_job2('Bob', 35, 5000, city='Beijing', job='Manager')


# 递归函数
def factorial_tail_recursion(n, f=1):
    if not isinstance(n, int):
        raise TypeError('bad operand type')
    if n < 0:
        raise ValueError('negative operand')
    if n <= 1:
        return f
    else:
        return factorial_tail_recursion(n - 1, f * n)  # python不会做尾递归优化


print(factorial(100))
print(factorial_tail_recursion(100))


# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
        return
    move(n - 1, a, c, b)
    move(1, a, b, c)
    move(n - 1, b, a, c)


# 期待输出:
# A --> C
# A --> B
# C --> B
# A --> C
# B --> A
# B --> C
# A --> C
move(3, 'A', 'B', 'C')
