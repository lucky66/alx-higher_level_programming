#!/usr/bin/python3
"""
7-model_state_fetch_all module

"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

"""
Script that lists all State objects from the database - Using module SQLAlchemy
"""

if __name__ == "__main__":
    conn = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    states = session.query(State).order_by(State.id)
    for state in states:
        print(state.id, state.name, sep=": ")
