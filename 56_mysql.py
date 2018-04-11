#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import mysql.connector
from contextlib import closing

user = input('Enter MySQL username:')
password = input('Enter MySQL password:')

with closing(mysql.connector.connect(user=user, password=password)) as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('DROP DATABASE IF EXISTS test')
        cursor.execute('CREATE DATABASE test')
        cursor.execute('USE test')
        cursor.execute('CREATE TABLE user (id VARCHAR(20) PRIMARY KEY,name VARCHAR(20))')
        cursor.execute('INSERT INTO user (id,name) VALUES (%s,%s)', ['1', 'Michael'])
        print(cursor.rowcount)
    conn.commit()

with closing(mysql.connector.connect(user=user, password=password, database='test')) as conn:
    with closing(conn.cursor()) as cursor:
        cursor.execute('SELECT * FROM user WHERE id=%s', ('1',))
        values = cursor.fetchall()
        print(values)
