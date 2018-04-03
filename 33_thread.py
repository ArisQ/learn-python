#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import threading
import random

s = 0


def threading_loop(lock):
    global s
    print('thread %s is running...' % threading.current_thread().name)
    i = 0
    if not (lock is None):
        for i in range(100000):
            lock.acquire()
            try:
                s = s + i
                s = s - i
            finally:
                lock.release()
    else:
        for i in range(100000):
            s = s + i
            s = s - i
    print('thread %s loop %d times, s=%d' % (threading.current_thread().name, i, s))


def threading_test(use_lock=False):
    print('threading_test, use_lock: %s' % use_lock)
    global s
    s = 0
    t = []
    lock = None
    if use_lock:
        lock = threading.Lock()
    for i in range(100):
        ti = threading.Thread(target=threading_loop, args=(lock,))
        t.append(ti)
    for ti in t:
        ti.start()
    print('threads are running, please wait')
    for ti in t:
        ti.join()
    print('threading_test finished, s=%d' % s)


local_s = threading.local()


def thread_local_loop():
    local_s.s = random.random()
    print('thread_local_loop %s running, local_s=%s' % (threading.current_thread().name, local_s.s))


def thread_local_test():
    local_s.s = 10
    print('thread_local_test(%s) is running, local_s=%d' % (threading.current_thread().name, local_s.s))
    t1 = threading.Thread(target=thread_local_loop)
    t2 = threading.Thread(target=thread_local_loop)
    t1.start()
    t2.start()
    t1.join()
    t2.join()


if __name__ == '__main__':
    threading_test()
    threading_test(True)
    thread_local_test()
