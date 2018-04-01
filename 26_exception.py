#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from functools import reduce


def str2num(s):
    return int(s)  # Traceback 4


def calc(exp):
    ss = exp.split('+')
    ns = map(str2num, ss)
    return reduce(lambda acc, x: acc + x, ns)  # Traceback 3


def main():
    r = calc('100 + 200 + 345')
    print('100 + 200 + 345 =', r)
    r = calc('99 + 88 + 7.6')  # Traceback 2
    print('99 + 88 + 7.6 =', r)


main()  # Traceback 1
