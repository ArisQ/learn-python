#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
for d in [b'World', b'Michael', b'Tracy']:
    s.sendto(d, ('127.0.0.1', 9999))
    print(s.recv(1024).decode('utf-8'))
s.close()
