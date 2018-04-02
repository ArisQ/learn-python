#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def fork_test():
    print('fork_test...')
    import os, platform, time
    if os.name != 'posix':
        print('fork unsupported')
    pid = os.fork()
    if pid == 0:
        print('[fork] child process(%d), parent id= %d' % (os.getpid(), os.getppid()))
        exit()
    else:
        print('[fork] fork finished(%d), child id= %d' % (os.getpid(), pid))
        os.wait()
    print('end of fork_test')


def multiprocessing_test():
    print('multiprocessing_test...')
    process_test()
    pool_test()
    queue_test()
    print('end of multiprocessing_test')


def process_test():
    print('process_test...')
    import multiprocessing, time

    def loop_proc(count):
        for i in range(count):
            print('looping[%s][%d]...' % (multiprocessing.current_process().name, i))
            time.sleep(0.5)

    p1 = multiprocessing.Process(target=loop_proc, args=(5,))
    p2 = multiprocessing.Process(target=loop_proc, args=(6,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    print('end of process_test')


def pool_loop(count):
    import time, multiprocessing
    for i in range(count):
        print('pool looping[%s][%d/%d]...' % (multiprocessing.current_process().name, i, count))
        time.sleep(0.1)


def pool_test():
    print('pool_test...')
    import multiprocessing, time
    p = multiprocessing.Pool()
    for i in range(10):
        p.apply_async(pool_loop, args=(i,))
    p.close()
    p.join()
    print('end of pool_test')


def queue_test():
    print('queue_test...')
    import multiprocessing, os, time, random
    q = multiprocessing.Queue()

    def write(q):
        print('Writing, process=%d' % os.getpid())
        for value in range(int(1 + random.random() * 10)):
            print('Put %d to queue' % value)
            q.put(value)
            time.sleep(random.random())

    def read(q):
        print('Reading, process=%d' % os.getpid())
        while True:
            value = q.get(True)
            print('Get %d from queue.' % value)

    pw = multiprocessing.Process(target=write, args=(q,))
    pr = multiprocessing.Process(target=read, args=(q,))
    pw.start()
    pr.start()
    pw.join()
    pr.terminate()
    print('end of queue_test')


def subprocess_test():
    print('subprocess_test...')
    import subprocess
    print('===== nslookup www.python.org =====')
    r = subprocess.call(['nslookup', 'www.python.org'])
    print('Exit code:', r)
    print('===== nslookup =====')
    p = subprocess.Popen(['nslookup'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, err = p.communicate(b'set q=mx\npython.org\nexit\n')
    print(output.decode('utf-8'))
    print('Exit code:', p.returncode)
    print('end of subprocess_test')


if __name__ == '__main__':
    fork_test()
    multiprocessing_test()
    subprocess_test()
