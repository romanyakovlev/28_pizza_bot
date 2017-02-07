from new_insert import Pizza, Choice, db
from json_file import catalog

if __name__ == "__main__":
    for pizza in catalog:
        choices_list = [Choice(title=choice['title'], price=choice['price'])
                        for choice in pizza['choices']]
        pizza_object = Pizza(title=pizza['title'],
                             description=pizza['description'],
                             choices=choices_list)
        db.session.add(*choices_list)
        all_choices = Choice.query.all()
        for choice in choices_list:
            if choice not in all_choices:
                db.session.add(choice)
        db.session.add(pizza_object)
    db.session.commit()
