#!/usr/bin/python3
"""
class definition of a State and an instance
 Base = declarative_base()
"""

if __name__ == '__main__':
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    import sys

    search_name = sys.argv[4]
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    first = session.query(State).filter(
        State.name == search_name).first()
    if first:
        print(f'{first.id}')

    else:
        print('Not found')
    session.close()
