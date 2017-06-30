#  app/__init__.py
""" Initialization file """
from flask import Flask

APP = Flask(__name__)

from app import views

APP.config.from_object('config')