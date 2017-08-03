from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)
try:
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['db_uri']
except KeyError as e:
    raise e
app.secret_key = 'super secret key'
db = SQLAlchemy(app)
