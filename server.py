from flask_admin import Admin, expose
from models import Pizza, Choice
from flask_admin.contrib.sqla import ModelView
from app import app, db
from flask import redirect, request, Response
import flask_admin
import os


response_code = 401


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == admin_username and password == admin_password


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', response_code,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


class MicroBlogModelView(ModelView):

    def is_accessible(self):
        auth = request.authorization
        auth_params_recieved = bool(auth)
        if auth_params_recieved:
            if check_auth(auth.username, auth.password):
                return True
        return False

    def inaccessible_callback(self, *args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()


class MyAdminIndexView(flask_admin.AdminIndexView):

    @expose('/')
    def index(self):
        auth_params_recieved = bool(request.authorization)
        self._template_args['auth_params_recieved'] = auth_params_recieved
        return super(MyAdminIndexView, self).index()

    def is_accessible(self):
        auth = request.authorization
        auth_params_recieved = bool(auth)
        if auth_params_recieved:
            if check_auth(auth.username, auth.password):
                return True
        return False

    def inaccessible_callback(self, *args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()


@app.route('/')
def index():
    return redirect('/admin/')


if __name__ == "__main__":
    try:
        admin_username = os.environ['username']
        admin_password = os.environ['password']
    except KeyError as e:
        raise e
    admin = Admin(app, index_view=MyAdminIndexView(), name='Admin_panel', template_mode='bootstrap3')
    admin.add_view(MicroBlogModelView(Pizza, db.session, endpoint="pizza"))
    admin.add_view(MicroBlogModelView(Choice, db.session, endpoint="choice"))
    app.run()
    db.session.commit()
