#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()
result_queue = queue.Queue()


class QueueManager(BaseManager):
    pass


QueueManager.register('get_task', callable=lambda: task_queue)
QueueManager.register('get_result', callable=lambda: result_queue)
manager = QueueManager(address=('', 5000), authkey=b'TheKey')
manager.start()
task = manager.get_task()
result = manager.get_result()
for i in range(10):
    print('Put task %d...' % i)
    task.put(i)
print('Get results...')
for i in range(10):
    r = result.get()
    print('Result: %s' % r)
manager.shutdown()
print('master exit.')
