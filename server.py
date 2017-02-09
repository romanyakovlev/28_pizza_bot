from flask_admin import Admin
from models import Pizza, Choice
from flask_admin.contrib.sqla import ModelView
from app import app, db
from flask import redirect, request, url_for


class MicroBlogModelView(ModelView):

    def is_accessible(self):
        return False

    def inaccessible_callback(self, name, **kwargs):
        print('asdf')
        return 'asdf'
        # redirect to login page if user doesn't have access
        return redirect(url_for('login', next=request.url))


if __name__ == "__main__":
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(MicroBlogModelView(Pizza, db.session))
    admin.add_view(MicroBlogModelView(Choice, db.session))
    app.run(port=8088)
    db.session.commit()
