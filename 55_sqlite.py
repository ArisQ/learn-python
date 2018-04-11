#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import os
from contextlib import closing

with sqlite3.connect('test.db') as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY,name VARCHAR(20))')
        cursor.execute('INSERT INTO user (id,name) VALUES (\'1\',\'Michael\')')
        print(cursor.rowcount)
    conn.commit()

with sqlite3.connect('test.db') as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT * FROM user WHERE id=?', ('1',))
        values = cursor.fetchall()
        print(values)

with sqlite3.connect('test.db') as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('DROP TABLE user')
        print(cursor.rowcount)
    conn.commit()

db_file = os.path.join(os.path.dirname(__file__), 'question.db')
if os.path.isfile(db_file):
    os.remove(db_file)

# 初始数据:
conn = sqlite3.connect(db_file)
cursor = conn.cursor()
cursor.execute('CREATE TABLE user(id VARCHAR(20) PRIMARY KEY, name VARCHAR(20), score INT)')
cursor.execute(r"INSERT INTO user VALUES ('A-001', 'Adam', 95)")
cursor.execute(r"INSERT INTO user VALUES ('A-002', 'Bart', 62)")
cursor.execute(r"INSERT INTO user VALUES ('A-003', 'Lisa', 78)")
cursor.close()
conn.commit()
conn.close()


def get_score_in(low, high):
    """ 返回指定分数区间的名字，按分数从低到高排序 """
    with sqlite3.connect(db_file) as conn:
        with closing(conn.cursor()) as cursor:
            cursor.execute('SELECT name FROM user WHERE score>=? AND score<=? ORDER BY score', (low, high))
            names = cursor.fetchall()
            return [n[0] for n in names]


# 测试:
assert get_score_in(80, 95) == ['Adam'], get_score_in(80, 95)
assert get_score_in(60, 80) == ['Bart', 'Lisa'], get_score_in(60, 80)
assert get_score_in(60, 100) == ['Bart', 'Lisa', 'Adam'], get_score_in(60, 100)

print('Pass')
