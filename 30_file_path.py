#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import stat
from functools import reduce


def mode2str(mode):
    mode_str = ['-', 'r', 'w', 'x', 'r', 'w', 'x', 'r', 'w', 'x']
    mode_priority = [stat.S_IRUSR, stat.S_IWUSR, stat.S_IXUSR,
                     stat.S_IRGRP, stat.S_IWGRP, stat.S_IXGRP,
                     stat.S_IROTH, stat.S_IWOTH, stat.S_IXOTH]
    if stat.S_IFMT(mode) == stat.S_IFDIR:
        mode_str[0] = 'd'
    for i in range(9):
        if (mode_priority[i] & mode) != mode_priority[i]:
            mode_str[i + 1] = '-'
        i += 1
    return reduce(lambda x, y: x + y, mode_str)


def dir_l(path):
    for f in sorted(os.listdir(path)):
        fstat = os.stat(f)
        print(mode2str(fstat.st_mode),
              '1', fstat.st_uid,
              fstat.st_gid,
              fstat.st_size,
              time.strftime('%b %d %H:%M', time.localtime(fstat.st_ctime)),
              f)
    pass

dir_l('.')


# 编写一个程序，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出相对路径。
def find_file(path, str):
    pass


find_file('.', 'txt')
