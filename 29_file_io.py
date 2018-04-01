#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import platform

filePath = ''
if platform.system() == 'Linux':
    filePath = r'/etc/passwd'
elif platform.system() == 'Windows':
    filePath = r'C:\Windows\system.ini'

with open(filePath, 'r') as f:
    s = f.read()
    print(s)
