from app import db


string_length_fifty = 50
string_length_hundred = 100


class Pizza(db.Model):
    pizza_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(string_length_fifty))
    description = db.Column(db.String(string_length_hundred))
    choices = db.relationship('Choice', backref='pizza', lazy='dynamic')

    def __repr__(self):
        return " Пицца '{}'".format(self.title)


class Choice(db.Model):
    choices_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(string_length_fifty))
    price = db.Column(db.Integer)
    pizza_id = db.Column(db.String(string_length_hundred), db.ForeignKey('pizza.pizza_id'))

    def __repr__(self):
        return "{} за {}руб для {}".format(self.title, self.price, Pizza.query.get(self.pizza_id))
