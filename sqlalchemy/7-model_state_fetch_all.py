#!/usr/bin/python3
"""
list all States objects from the database hbtn_0e_6_usa
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import  sessionmaker

connection_string = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])
engine = create_engine(connection_string)
Session = sessionmaker(bind=engine)
session = Session()

if __name__ == '__main__':
    for instance in session.query(State).order_by(State.id):
        print(instance.id, instance.name, sep=": ")
