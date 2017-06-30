""" Views.py """
from flask import render_template

from app import APP

@APP.route('/')
def index():
    return render_template("login.html")

@APP.route('/about')
def home():
    return render_template("signup.html")
    