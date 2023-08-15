from . import app   # The `app` first is the directory, the second is the `app` function inside of the `__init__.py`
from flask import render_template

@app.route('/') # This is a decorator.
@app.route('/index') # You can chain decorators.
def index():
  user = {'username': 'Dion'}
  posts = [
    {
      'author': {'username': 'John'},
      'body': 'Beautiful day!'
    },
    {
      'author': {'username': 'Henny'},
      'body': 'Als je wint, heb je vrienden'
    }
  ]
  return render_template('index.html', user=user, title="Home Page", posts=posts) # The first `user` is the variable used in the Jinja2 template, the secons is the Python variable defined.

