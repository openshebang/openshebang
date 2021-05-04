import os 
import json # Hier staat alle config in JSON voor de productie server

with open('/etc/py/flask/openshebang.json') as config_file:
    config = json.load(config_file)


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
#    If the above `openshebang.json file is NOT used, uncomment both below config settings.`
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'heel_erg_geheim...NOT'
#    SECRET_KEY = config.get('SECRET_KEY') # Get the info from the JSON-file

    SQLALCHEMY_DATABASE_URI = 'sqlite:///'+os.path.join(basedir, config.get('SQLALCHEMY_DATABASE_URI'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False # Otherwise always there will be a signal to the application when a change has been made.
    MAIL_SERVER = os.environ.get('MAIL_SERVER')
    MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    ADMINS = ['dion@dresschers.net']
    UPLOAD_FOLDER = '/the/uploads'
    ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'md', 'svg'])
    MAX_CONTENT_LENGTH = 1024 * 1024
    UPLOAD_EXTENSIONS = ['.jpg', '.png', '.gif', '.svg', '.jpeg']
    UPLOAD_PATH = 'app/static/uploads' # The `app` part is NOT dynamic and should be made dynamic.... Make sure that you upload this file first!
