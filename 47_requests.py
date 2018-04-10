#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import requests

r = requests.get('https://www.baidu.com')
print('==========status_code==========')
print(r.status_code)
print('==========text==========')
print(r.text)
print('==========headers==========')
print(r.headers)
r = requests.get('https://www.baidu.com/s', params={'wd': 'python'})
print('==========url==========')
print(r.url)
print('==========encoding==========')
print(r.encoding)
print('==========content==========')
print(r.content)
r = requests.get('https://api.github.com/')
print('==========json==========')
print(r.json())
print('==========text==========')
print(r.text)
print('==========post text==========')
r = requests.post('https://api.github.com/')
print(r.text)
