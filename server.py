from flask_admin import Admin
from models import Pizza, Choice
from flask_admin.contrib.sqla import ModelView
from app import app, db

if __name__ == "__main__":
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(Pizza, db.session))
    admin.add_view(ModelView(Choice, db.session))
    app.run(port=8088)
    db.session.commit()
