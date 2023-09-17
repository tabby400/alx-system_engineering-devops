#!/usr/bin/python3
"""this module is a definition of a state model with
class definition of a state and instance Base = declarative_base()"""


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()

""" the state class then inherits from base"""


class State(Base):

    __tablename__ = 'states'  # database table
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)  # max length of chars 128
