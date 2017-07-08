""" Views.py """
from flask import render_template

from app import APP

class Main(object):
    """ Main application class for the application"""
    def __init__(self):
        self.users = {}
        self.currentuser = ''
        self.authenticated = False

    def adduser(self, username, password):
        ''' Adds signed up user to global dict of users '''
        if username in self.users:
            return ' User already exists'
        self.users[username] = password
        self.currentuser = username

    def loginuser(self, username, password):
        ''' checks availabilty of user credentials and logins in the person '''
        if self.users[username] == password:
            self.currentuser = username
            self.authenticated = True
        else:
            pass
    def logout(self):
        '''logs out users '''
        self.currentuser = ''
        self.authenticated = False

@APP.route('/')
def index():
    return render_template("login.html")

@APP.route('/about')
def home():
    return render_template("signup.html")
    