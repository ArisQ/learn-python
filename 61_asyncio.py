#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import asyncio


@asyncio.coroutine
def hello():
    print('Hello First! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello Second! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello Third! (%s)' % threading.currentThread())


async def hello_async_await():
    print('async/await first! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('async/await second! (%s)' % threading.currentThread())
    await asyncio.sleep(1)
    print('async/await third! (%s)' % threading.currentThread())


loop = asyncio.get_event_loop()
task = [hello() for i in range(5)]
task_async_await = [hello_async_await() for i in range(5)]
loop.run_until_complete(asyncio.wait(task))
loop.run_until_complete(asyncio.wait(task_async_await))
loop.close()
