"""
Anything the user can navigate to, goes here, with the exception of auth stuff
"""

from flask import Blueprint, render_template

views = Blueprint('views', __name__)  # Blueprint('name_of_blueprint', __name__)


@views.route('/')
def home():
    return render_template("home.html")


@views.route('/base')
def base():
    return "<h1>Base Test. <a href='/'>Click here to go back.</a></h1>"
