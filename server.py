from flask_admin import Admin, expose
from models import Pizza, Choice
from flask_admin.contrib.sqla import ModelView
from app import app, db
from flask import redirect, request, Response
import flask_admin
import os

try:
    admin_username = os.environ['username']
    admin_password = os.environ['password']
except KeyError:
    undefined_keys = []
    if not os.environ.get('username', None):
        undefined_keys.append('username')
    if not os.environ.get('password', None):
        undefined_keys.append('password')
    print('KeyError: key(s) {}'.format(', '.join(undefined_keys)))


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == admin_username and password == admin_password


def authenticate():
    """Sends a 401 response that enables basic auth"""
    return Response(
    'Could not verify your access level for that URL.\n'
    'You have to login with proper credentials', 401,
    {'WWW-Authenticate': 'Basic realm="Login Required"'})


class MicroBlogModelView(ModelView):

    def is_accessible(self):
        auth = request.authorization
        auth_params_recieved = bool(auth)
        if auth_params_recieved:
            if check_auth(auth.username, auth.password):
                return True
        return False

    def inaccessible_callback(self, name, **kwargs):
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

    def inaccessible_callback(self, name, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()


@app.route('/')
def index():
    return redirect('/admin/')


if __name__ == "__main__":
    admin = Admin(app, index_view=MyAdminIndexView(), name='Admin_panel', template_mode='bootstrap3')
    admin.add_view(MicroBlogModelView(Pizza, db.session, endpoint="pizza"))
    admin.add_view(MicroBlogModelView(Choice, db.session, endpoint="choice"))
    app.run()
    db.session.commit()
