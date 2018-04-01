#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from enum import Enum, unique

Week = Enum('Week', ('Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday'))
print(Week)
print(Week.Sunday)
print(Week(2))
print(Week['Tuesday'])
for name, mem in Week.__members__.items():
    print(mem.value, name, mem)


@unique
class Weekday(Enum):
    Sun = 0
    Mon = 1
    Tue = 2
    Wed = 3
    Thu = 4
    Fri = 5
    Sat = 6


class Gender(Enum):
    Male = 0
    Female = 1


class Student(object):
    def __init__(self, name, gender):
        if not isinstance(gender, Gender):
            raise TypeError('bad gender type')
        self.name = name
        self.gender = gender


# 测试:
bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')
