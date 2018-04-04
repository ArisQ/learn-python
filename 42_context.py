#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import contextlib


class ContextedClass(object):
    def __enter__(self):
        print('entering')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type:
            print('Error')
        else:
            print('exiting')

    def work(self):
        print('contexted working...')


with ContextedClass() as cc:
    cc.work()


class NonContextedClass(object):
    def work(self):
        print('non contexted working...')

    def close(self):
        print('closing')


@contextlib.contextmanager
def create_noncontexted_class():
    print('entering')
    yield NonContextedClass()
    print('exiting')


with create_noncontexted_class() as ncc:
    ncc.work()

with contextlib.closing(NonContextedClass()) as ncc:
    ncc.work()
