# This is created for OpenSheBang and not for the individual apps.
import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dummy' # This is used by `pip install flask-wtf`, to prevent in forms Cross Site Request Forgery. 