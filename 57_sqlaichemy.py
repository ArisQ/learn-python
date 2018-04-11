#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from sqlalchemy import Column, String, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class User(Base):
    __tablename__ = 'user'
    id = Column(String(20), primary_key=True)
    name = Column(String(20))


username = input('Enter MySQL username:')
password = input('Enter MySQL password:')
engine = create_engine('mysql+mysqlconnector://%s:%s@localhost:3306/test' % (username, password))
DBSession = sessionmaker(bind=engine)
session = DBSession()
session.add(User(id='5', name='Bob'))
session.commit()
print('==========after add==========')
for u in session.query(User).all():
    print(u.id, u.name)
print('==========query==========')
user = session.query(User).filter(User.id == '5').one()
print(user.id, user.name)
session.delete(user)
session.commit()
print('==========after delete==========')
for u in session.query(User).all():
    print(u.id, u.name)
session.close()
