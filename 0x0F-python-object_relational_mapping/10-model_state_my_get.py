#!/usr/bin/python3

"""
this is able toprint the state object with name
passed as argument from database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from model_state import State
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    session_maker = sessionmaker(bind=engine)
    session = session_maker()

    for state in session.query(State):
        if sys.argv[4] == state.name:
            print("{}".format(state.id))
            break
    else:
        print("Not found")  # display
