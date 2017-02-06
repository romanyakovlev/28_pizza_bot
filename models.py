from insert_to_db import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import json


engine = create_engine('sqlite:///foo.db')
Session = sessionmaker(bind=engine)
session = Session()
catalog = session.query(User).all()
session.commit()
for x in catalog:
    x.choices = json.loads(x.choices)
