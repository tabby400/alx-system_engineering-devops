#!/usr/bin/python3
"""this module is used when deleting all states objects
with a name containing letter a"""


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sys import argv

if __name__ == "__main__":

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                        argv[2],
                                                        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    output = session.query(State).filter(State.name.like("%a%"))\
                                 .delete(synchronize_session='fetch')
    session.commit()  # delete states with a
    session.close()
