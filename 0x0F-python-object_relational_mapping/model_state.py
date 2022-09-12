#!/usr/bin/python3
"""contains the class definition of a State and an instance Base = declarative_base()"""

import sys
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Sequence, Column,Integer, String
from sqlalchemy import (create_engine)

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'

    id = Column(Integer, Sequence('state_id_seq'),
                primary_key=True, unique=True,
                 nullable=False, autoincrement=True)

    name = Column(String(128), nullable=False)


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
