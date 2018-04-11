#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wsgiref.simple_server import make_server
import threading


def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return [b'<h1>Hello, Web!</h1>']


def application2(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]


threading.Thread(target=lambda: make_server('', 8000, application).serve_forever()).start()
threading.Thread(target=lambda: make_server('', 8001, application2).serve_forever()).start()
