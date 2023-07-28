#!/usr/bin/python3
"""
python file that contains class definition of a State and an 
instance Base = declarative_base()
"""
import sys
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#connection_string = 'mysql+mysqldb://{}.{}@localhost/{}'.format(sys.argv[1], sys.argv[2], sys.argv[3])

#engine = create_engine(connection_string)

Base = declarative_base()
#Session = sessionmaker(bind=engine)
#session = Session()


class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
