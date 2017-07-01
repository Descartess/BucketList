""" Views.py """
from flask import render_template

from app import APP

@APP.route('/')
def index():
    return render_template("login.html")

@APP.route('/about')
def home():
    return render_template("signup.html")

class Users(object):
    """ Users class that holds all user actions """
    def signup(self, username, password):
        """ Signs Up a user """
        return username, password

class Main(Users):
    """ Main application class for the application"""
    def __init__(self):
        self.users = {}

    def adduser(self, username, password):
        ''' Adds signed up user to global dict of users '''
        user = self.signup(username, password)
        self.users[user[0]] = user[0]
