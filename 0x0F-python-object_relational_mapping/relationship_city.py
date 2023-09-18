#!/usr/bin/python3
"""
this is a definition of city model that inherits
 from sqlqlchemy base
"""

from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """Representing a city for MySQL database.

    Attr:
        id (sqlalchemy.Column): city id.
        name (sqlalchemy.Column): city name.
        state_id (sqlalchemy.Column): city's state id.
    """
    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
