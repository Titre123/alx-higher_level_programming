#!/usr/bin/python3
"""contains the class definition of a State and an instance Base = declarative_base()"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence, Column,Integer, String

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'),
                primary_key=True, unique=True,
                 nullable=False, autoincrement=True)

    name = Column(String(128), nullable=False)
