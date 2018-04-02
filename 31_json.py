#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json

obj = dict(name='小明', age=20)
s = json.dumps(obj, ensure_ascii=True)
print(s)
s2 = json.dumps(obj, ensure_ascii=False)
print(s2)

o = json.loads(s)
print(o)
o2 = json.loads(s2)
print(o2)
