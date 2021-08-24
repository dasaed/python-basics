"""
Auth related URLs go here
"""

from flask import Blueprint

auth = Blueprint('auth', __name__)  # Blueprint('name_of_blueprint', __name__)
# ^ just creates a Blueprint object with the name of auth.


@auth.route('/login')
def login():
    return "<p>Login</p>"


@auth.route('/logout')
def logout():
    return "<p>Logout</p>"


@auth.route('/sign-up')
def sign_up():
    return "<p>Sign Up</p>"


