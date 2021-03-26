from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

app = Flask(__name__)
app.config.from_object(Config) # De .config is de method
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' # Flask-Login needs to know what the view function is that handles logins.

from app import routes # De routes is `app\routes.py`. Deze moet onderaan.
from app import models # This modesl will define the structure of the database.


