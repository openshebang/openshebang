from app import app # The `app` first is the directory, the second is the `app` function inside of the `__init__.py`
from flask import render_template

@app.route('/') # This is a decorator.
@app.route('/index') # You can chain decorators.
def index():
  user = {'username': 'Dion'}
  title = "Main"
  return render_template('index.html', user=user, title="Home Page") # The first `user` is the variable used in the Jinja2 template, the secons is the Python variable defined.

