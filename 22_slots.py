#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from types import MethodType


class Student(object):
    __slots__ = ('name', 'age')


s = Student()
s.name = 'Michael'
print(s.name)

s2 = Student()
try:
    print(s2.name)
except AttributeError as e:
    print('s2 has no attribute', e)

Student.name = 'John'
try:
    print(s2.name)
except AttributeError as e:
    print('s2 has no attribute', e)


def set_age(self, age):
    self.age = age


try:
    s.set_age = MethodType(set_age, s)
except AttributeError as e:
    print(e)
