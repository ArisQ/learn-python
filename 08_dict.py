#!/usr/bin/env python3
# -*- coding: utf-8 -*-

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d)
print(d['Michael'])
d['Adam'] = 67
print(d)
d['Bob'] = 90
print(d)
print('Thomas' in d)  # False
print(d.get('Thomas'))  # None
print(d.get('Thomas', -1))  # -1
print(d.pop('Bob'))
print(d)
