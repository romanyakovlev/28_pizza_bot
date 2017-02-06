from sqlalchemy import create_engine, Integer, String, Column
from create_db import users, metadata
import json
from json_file import catalog
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///foo.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    choices = Column(String)


if __name__ == "__main__":
    session = Session()
    for x in catalog:
        ed_user = User(title=x['title'], description=x['description'], choices=json.dumps(x['choices']))
        session.add(ed_user)
    session.commit()
