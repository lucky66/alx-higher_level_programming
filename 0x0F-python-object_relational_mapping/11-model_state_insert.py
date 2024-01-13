#!/usr/bin/python3
"""
11-model_state_insert module

"""
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv

"""
Script that adds the State object “Louisiana” to the database
Using module SQLAlchemy
"""

if __name__ == "__main__":
    conn = "mysql://{}:{}@localhost:3306/{}"
    engine = create_engine(conn.format(argv[1], argv[2], argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()
    print(new_state.id)
