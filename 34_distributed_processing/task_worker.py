#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task', callable=lambda: task_queue)
QueueManager.register('get_result', callable=lambda: result_queue)
manager = QueueManager(address=('localhost', 5000), authkey=b'TheKey')
try:
    manager.connect()
except ConnectionRefusedError:
    print('Start task master first.')
    exit(0)

task = manager.get_task()
result = manager.get_result()
for i in range(5):
    try:
        n = task.get()
        print('running task %d * %d' % (n, n))
        r = '%d*%d=%d' % (n, n, n * n)
        time.sleep(1)
        result.put(r)
    except queue.Empty:
        print('task queue is empty.')

print('worker exit.')
