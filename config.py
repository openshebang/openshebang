import os # needed for importing the environment variables

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'test_as_environment_variable_SECRET_KEY_is_not_set'