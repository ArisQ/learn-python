#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import stat
import platform
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
        f_stat = os.stat(os.path.join(path, f))
        owner_name = f_stat.st_uid
        owner_group = f_stat.st_gid
        if platform.system() == 'Linux':
            import pwd, grp
            owner_name = pwd.getpwuid(f_stat.st_uid).pw_name
            owner_group = grp.getgrgid(f_stat.st_gid).gr_name
        print('%s %d %s %s %5d %s %s' % (mode2str(f_stat.st_mode),
                                         f_stat.st_nlink,
                                         owner_name,
                                         owner_group,
                                         f_stat.st_size,
                                         time.strftime('%b %d %H:%M', time.localtime(f_stat.st_ctime)),
                                         f))


def find_file(path, str):
    result = []
    for f in os.listdir(path):
        if os.path.isfile(f) and f.find(str) != -1:
            result.append(os.path.join(path, f))
        if os.path.isdir(f):
            sub_result = find_file(os.path.join(path, f), str)
            if sub_result:
                result.append(sub_result)
    return result


if __name__ == '__main__':
    dir_l('.')
    print(find_file('.', '9'))
