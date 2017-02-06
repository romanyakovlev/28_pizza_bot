from flask import Flask
from flask_admin import Admin
from models import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
from flask_admin.contrib.sqla import ModelView
app.secret_key = 'super secret key'
# Flask and Flask-SQLAlchemy initialization here

engine = create_engine('sqlite:///foo.db')
Session = sessionmaker(bind=engine)
Base = declarative_base()
session = Session()

admin = Admin(app, name='microblog', template_mode='bootstrap3')
admin.add_view(ModelView(User, session))

app.run()

session.commit()
