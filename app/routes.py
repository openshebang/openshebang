from flask import render_template, flash, redirect, url_for
from app import app # The first 'app' is the app-Package represents with the dir 'app', in that is a 'app' variable in the __init__.py file.
from app.forms import LoginForm # The app.forms is the app folder, the forms.py file, the LoginForm class

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

@app.route('/login', methods=['GET', 'POST']) # GET is default, but the submittig the from it uses 'POST'
def login():
  form = LoginForm() # This is the wtform, which will be imported above
  if form.validate_on_submit(): # If the Submit button has been pushed.
    flash('Login requested for user {}, remember_me={}'.format(
        form.username.data, form.remember_me.data)) # flask is also from Flask and have to be imported above
    return redirect(url_for('index')) # go to the /index page, but this have to be imported above # Here the url_for() function has been used, that has to be imported above
  return render_template('login.html', title='Sign In', form=form)