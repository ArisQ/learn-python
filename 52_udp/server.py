#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind(('localhost', 9999))
while True:
    data, addr = s.recvfrom(1024)
    data = data.decode('utf-8')
    print('%s  ==> %s' % (addr, data))
    reply = 'Hello, %s!' % data
    print('%s <==  %s' % (addr, reply))
    s.sendto(reply.encode('utf-8'), addr)
s.close()
