from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
import logging # For logging
from logging.handlers import SMTPHandler # For the sender
from logging.handlers import RotatingFileHandler
import os

app = Flask(__name__)
app.config.from_object(Config) # De .config is de method
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login' # Flask-Login needs to know what the view function is that handles logins.

if not app.debug:
    if app.config['MAIL_SERVER']:
        auth = None
        if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
            auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
        secure = None
        if app.config['MAIL_USE_TLS']:
            secure = ()
        mail_handler = SMTPHandler(
            mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
            fromaddr='no-reply@' + app.config['MAIL_SERVER'],
            toaddrs=app.config['ADMINS'], subject='Microblog Failure',
            credentials=auth, secure=secure)
        mail_handler.setLevel(logging.ERROR) # Only log ERROR not all 
        app.logger.addHandler(mail_handler)

    # This will create a file will all the errors (INFO-messages to be more precise)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/openshebang.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('OpenShebang startup') # This will create a line in the logfile with the text 'OpenShebang startup', with the file on which it is was executed (which you will see in the 'logs/openshebang.log'-file)
    

from app import routes # De routes is `app\routes.py`. Deze moet onderaan. De routes.py file.
from app import models # This modesl will define the structure of the database. De models.py file.
from app import errors # Dit is de `app`, directory, de `errors.py`-file


