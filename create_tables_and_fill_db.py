from app import db
from models import Pizza, Choice
from json_file import catalog

if __name__ == "__main__":
    db.create_all()

    for pizza in catalog:
        choices_list = [Choice(title=choice['title'], price=choice['price'])
                        for choice in pizza['choices']]
        pizza_object = Pizza(title=pizza['title'],
                             description=pizza['description'],
                             choices=choices_list)
        db.session.add(*choices_list)
        db.session.add(pizza_object)
    db.session.commit()
