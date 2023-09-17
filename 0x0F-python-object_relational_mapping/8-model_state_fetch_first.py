#!/usr/bin/python3


"""this module prints the first object from the database
"""

from model_state import Base, State
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(argv[1],
                                                        argv[2],
                                                        argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    output = session.query(State).order_by(State.id).first()
    if output:
        print("{}: {}".format(output.id, output.name))
    else:
        print("Nothing")
    session.close()
