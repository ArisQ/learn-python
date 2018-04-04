#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(Point)
print(p)
print(p.x)
print(p.y)

q = deque(['a', 'b', 'c'])
print(q)
q.pop()
q.popleft()
q.append('x')
q.appendleft('y')
print(q)

dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd)
print(dd['key1'])
print(dd['key2'])

od = OrderedDict()
od['z'] = 1
od['y'] = 2
od['x'] = 3
print(od)
print(od.keys())
for k, v in od.items():
    print(k, v)

c = Counter()
for ch in 'programming':
    c[ch] = c[ch] + 1
print(c)
