import os
from flask import Flask, render_template, request, Response, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_wtf.csrf import CSRFProtect
from flask_migrate import Migrate


app = Flask(__name__)
csrf = CSRFProtect(app)


SECRET_KEY = os.urandom(32)
SQLALCHEMY_TRACK_MODIFICATIONS = False


basedir = os.path.abspath(os.path.dirname(__file__))




# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = "postgresql://postgres:Iamasoulwinner1@localhost:5432/fyyur"
SQLALCHEMY_TRACK_MODIFICATIONS = True