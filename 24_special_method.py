#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Student(object):
    def __init__(self, name='', bag_size=5):
        print('Initializing a student, name is', name)
        self.bag_iter = 0
        self.bag_size = bag_size

    def __str__(self):
        return 'This is a student'

    def __repr__(self):
        return '[Debug] This is just a student.'

    def __iter__(self):
        print('Just iter a student.')
        return self

    def __next__(self):
        if self.bag_iter >= self.bag_size:
            raise StopIteration()
        self.bag_iter += 1
        return self.bag_iter

    def __getitem__(self, item):
        return 'Just get yourself %s' % item

    def __setitem__(self, key, value):
        print('I can\'t remember it')

    def __delitem__(self, key):
        print('Delete what, %s ?' % key)

    def __getattr__(self, item):
        if item == 'dowork':
            print('I refuse to do this.')
            return lambda: 0
        print('I have no' + item)

    def __call__(self, *args, **kwargs):
        print('So what do you call a student for.')


j = Student('Jack')
print('Student:', j)
print('Student.__str__():', j.__str__())
print('Student.__repr__():', j.__repr__())
print('Student.__iter__():', j.__iter__())
print('=== for s in Student: ===')
for i in j:
    print(i, end=' ')
print('')
print('=== end for s in Student ===')
print('Student[0] (Student.__getitem__[0]):', j[0])
print('Student[0:1] (Student.__getitem__[0:1]):', j[0:1])
print('Student[0]=0 (Student.__setitem__[0]):', end=' ')
j[0] = 0
print('del Student[0] (Student.__delitem__[0]):', end=' ')
del j[0]
print('Student.nonexist:',j.nonexit)
print('Student.dowork:',j.dowork)
print('Student.dowork():',j.dowork())
print('Student():', end=' ')
j()
print('callable(Student):', callable(Student))
print('callable(Student()):', callable(j))
