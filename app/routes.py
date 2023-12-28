from flask import render_template
from app import app # The first 'app' is the app-Package represents with the dir 'app', in that is a 'app' variable in the __init__.py file.


@app.route('/') # This is a decorator, that conntect / to this function
@app.route('/index') # Second decorator
def index():
  user = {'username': 'dion'} # Just a user as the db does not exist yet.
  posts = [ # python list
    {
      'author': { 'username': 'John'},
      'body': 'Hey hello from John',
    },
    {
      'author': { 'username': 'Mimi'},
      'body': 'Mimimimimi',
    },
  ]
  # return "Hello" + user'username'
  return render_template('index.html', title='home', user=user, posts=posts) # The first argument is the argument used in the template, the second is what you define it here.