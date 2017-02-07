from sqlalchemy import create_engine, Integer, String, Column, ForeignKey

import json
from json_file import catalog
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

engine = create_engine('sqlite:///foo.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    addresses = relationship('Choices', back_populates="user")


class Choices(Base):
    __tablename__ = 'choices'
    id = Column(Integer, primary_key=True)
    parent_id = Column(Integer, ForeignKey('users.id'))
    Choice_string = Column(String)
    parent = relationship("User", back_populates="choices")


Base.metadata.create_all(engine)

if __name__ == "__main__":
    session = Session()
    for x in catalog:
        ed_user = User(title=x['title'], description=x['description'],
                       choices=json.dumps(x['choices']))
        session.add(ed_user)
    session.commit()
