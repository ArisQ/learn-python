#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import threading


def tcp_link(sock, addr):
    print('New Connection:', addr)
    sock.send(b'Welcome!')
    try:
        while True:
            data = sock.recv(1024)
            if not data or data.decode('utf-8') == 'exit':
                break
            data = data.decode('utf-8')
            print(data)
            sock.send(('Hello,%s!' % data).encode('utf-8'))
    except ConnectionResetError:
        print('disconnected')
    finally:
        sock.close()


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('127.0.0.1', 9999))
s.listen(5)
while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcp_link, args=(sock, addr))
    t.start()
