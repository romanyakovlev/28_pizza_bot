from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///foo.db'
db = SQLAlchemy(app)


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.String(100))
    choices = db.relationship('Choice', backref='pizza', lazy='dynamic')

    def __repr__(self):
        return " Пицца '{}'".format(self.title)


class Choice(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    price = db.Column(db.Integer)
    pizza_title = db.Column(db.String(100), db.ForeignKey('pizza.title'))

    def __repr__(self):
        return "Заказ '{} - {}'".format(self.title, self.price)


if __name__ == "__main__":
    db.create_all()
