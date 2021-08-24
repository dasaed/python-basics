from flask import Flask
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix='/')
    # localhost:5000[/,/base] = takes you to home page, or "base" page, without any prefix

    app.register_blueprint(auth, url_prefix='/authentication/')
    # localhost:5000/authentication[/login,/logout,/sign-up] = takes you to login/logout/sign-up page, but with
    # a /authentication/ prefix first

    return app