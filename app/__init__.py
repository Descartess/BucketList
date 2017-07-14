#  app/__init__.py
""" Initialization file """
from flask import Flask
from .views import app_blueprint

APP = Flask(__name__)

# from app import views
APP.register_blueprint(app_blueprint)

APP.config['DEBUG'] = True
