from flask import Flask
from flask_admin import Admin
from new_insert import Pizza, Choice, db
from flask_admin.contrib.sqla import ModelView


app = Flask(__name__)
app.secret_key = 'super secret key'

if __name__ == "__main__":
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(Pizza, db.session))
    admin.add_view(ModelView(Choice, db.session))
    app.run(port=8088)
    db.session.commit()
