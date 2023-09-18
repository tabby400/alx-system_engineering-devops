#!/usr/bin/python3

"""the module is used to add a new state object
to the database"""

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
    new_obj = State(name='Louisiana')  # to be added
    session.add(new_obj)
    session.commit()
    print(new_obj.id)
    session.close()
