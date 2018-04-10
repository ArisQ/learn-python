#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import psutil
import multiprocessing

# CPU信息
print(psutil.cpu_count())
print(psutil.cpu_count(logical=False))
print(psutil.cpu_times())
print(psutil.cpu_percent(interval=1, percpu=True))
# 内存信息
print(psutil.virtual_memory())
print(psutil.swap_memory())
# 磁盘信息
print(psutil.disk_partitions())
print(psutil.disk_usage('/'))
print(psutil.disk_io_counters())
# 网络信息
print(psutil.net_io_counters())
print(psutil.net_if_addrs())
print(psutil.net_if_stats())
print(psutil.net_connections())
# 进程信息
print(psutil.pids())
p = psutil.Process(multiprocessing.current_process().pid)
print(p.name())
print(p.exe())
print(p.cwd())
print(p.cmdline())
print(p.ppid())
print(p.parent())
print(p.children())
print(p.status())
print(p.username())
print(p.create_time())
# print(p.terminal()) # Unix Only
print(p.cpu_times())
print(p.memory_info())
print(p.open_files())
print(p.connections())
print(p.num_threads())
print(p.threads())
print(p.environ())
# print(p.terminate())  # 结束进程
# 模拟ps命令
psutil.test()
