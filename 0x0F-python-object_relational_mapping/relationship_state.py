#!/usr/bin/python3

""" this is a definition of state model that
inherits from sqlalchemy
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City
from sqlalchemy.orm import relationship
import sys

class State(Base):
    """Representing a state for  MySQL database.

    Attr:ibutes:
        __tablename__ (str): name of the MySQL table to store States.
        id (sqlalchemy.Integer): state's id.
        name (sqlalchemy.String): state's name.
        cities (sqlalchemy.orm.relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
