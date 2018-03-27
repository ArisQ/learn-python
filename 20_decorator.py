#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time, functools

print(abs.__name__)


def log1(func):
    def wrapper(*args, **kw):
        print('calling %s()' % func.__name__)
        return func(*args, **kw)

    return wrapper


@log1  # 等价于now=log(now)
def now1():
    print('2018-3-27')


def log2(text):
    def decorator(func):
        def wrapper(*args, **kw):
            print('calling %s(), message %s' % (func.__name__, text))
            return func(*args, **kw)

        return wrapper

    return decorator


@log2('nothing')
def now2():
    print('2018-3-27')


def log3(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('calling %s(), message %s' % (func.__name__, text))
            return func(*args, **kw)

        return wrapper

    return decorator


@log3('everything')
def now3():
    print('2018-3-27')


now1()
print(now1.__name__)
now2()
print(now2.__name__)
now3()
print(now3.__name__)


def metric(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        start = time.time()
        result = fn(*args, **kw)
        end = time.time()
        print('%s executed in %s ms' % (fn.__name__, (end - start) * 1000))
        return result

    return wrapper


# 测试
@metric
def fast(x, y):
    time.sleep(0.0012)
    return x + y


@metric
def slow(x, y, z):
    time.sleep(0.1234)
    return x * y * z


f = fast(11, 22)
s = slow(11, 22, 33)
if f != 33:
    print('测试失败!')
elif s != 7986:
    print('测试失败!')


def print_begin_end(fn):
    @functools.wraps(fn)
    def wrapper(*args, **kw):
        print('begin call %s' % fn.__name__)
        result = fn(*args, **kw)
        print('end call %s' % fn.__name__)
        return result

    return wrapper


@print_begin_end
def now4():
    print('2018-3-27')


now4()
print(now4.__name__)


def log5(text=''):
    def decorator(fn):
        @functools.wraps(fn)
        def wrapper(*args, **kw):
            print('calling %s, message %s' % (fn.__name__, text))
            return fn(*args, **kw)

        return wrapper
    return decorator


@log5()
def now5():
    pass


@log5('whatever')
def now6():
    pass


now5()
print(now5.__name__)
now6()
print(now6.__name__)
#
# 请编写一个decorator，能在函数调用的前后打印出'begin call'和'end call'的日志。
#
# 再思考一下能否写出一个@log的decorator，使它既支持：
#
# @log
# def f():
#     pass
# 又支持：
#
# @log('execute')
# def f():
#     pass
