#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import asyncio
from aiohttp import web


async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(body=b'<h1>Index</h1>', content_type='text/html')


async def hello(request):
    await asyncio.sleep(0.5)
    body = '<h1>Hello, %s!</h1>' % request.match_info['name']
    return web.Response(body=body.encode('utf-8'), content_type='text/html')


print('http://localhost:8000')
print('http://localhost:8000/hello/world')
loop = asyncio.get_event_loop()
app = web.Application(loop=loop)
app.router.add_route('GET', '/', index)
app.router.add_route('GET', '/hello/{name}', hello)
srv = loop.create_server(app.make_handler(), '127.0.0.1', 8000)
loop.run_until_complete(srv)
loop.run_forever()
