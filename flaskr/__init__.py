import os

from flask import Flask

# c1.3.2 'Application Setup'
def create_app(test_config=None):
  # create and configure the app
  app = Flask(__name__, instance_relative_config=True) # c1.3.2 p21
  app.config.from_mapping(
    SECRET_KEY='dev', # c1.3.2 p11
    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'), # c1.3.2 p21
    )
  
  if test_config is None:
    # load the instance config, if it exists, when not testing
    app.config.from_pyfile('config.py', silent=True)
  else:
    # load the test config if passed in
    app.config.from_mapping(test_config)
  
  # ensure the instance folder exists
  try:
    os.makedirs(app.instance_path) # c1.3.2 p22
  except OSError:
    pass

  # a simple page that says hello
  @app.route('/hello') # c1.3.2 p12
  def hello():
    return 'Hello, World!'
  
  # Return the app # c1.3.2 p23Run with `flask --app flaskr run --debug` 
  return app
# /c1.3.2 'Application Setup'