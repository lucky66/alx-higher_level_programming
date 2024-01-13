#!/usr/bin/python3
"""
13-model_state_delete_a module
"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv


"""
Script that deletes all State objects with a name containing
the letter a from the database
Using module SQLAlchemy
"""

if __name__ == "__main__":
    conn = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).filter(State.name.like('%a%'))
    for state in states:
        session.delete(state)
    session.commit()
