#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading


def recv_thread(q):
    try:
        while True:
            data = s.recv(1024)
            if data:
                print(data.decode('utf-8'))
            else:
                break
    except ConnectionAbortedError:
        print('disconnected')


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('127.0.0.1', 9999))
threading.Thread(target=recv_thread, args=(s,)).start()
while True:
    data = input()
    s.send(data.encode('utf-8'))
    if data == 'exit':
        break
s.close()
