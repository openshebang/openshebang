from . import app   # The `app` first is the directory, the second is the `app` function inside of the `__init__.py`
from flask import render_template
from blog.forms import LoginForm # The `form` is the `forms.py`-file.
from flask import flash
from flask import redirect
from flask import url_for

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

@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm() # You have to import this first above.
  if form.validate_on_submit(): # If the user sends all required info in the Form.
    flash('Login requested fr user {}, rememberme={}'.format(form.username.data, form.remember_me.data)) # The `data` is all the data that the user entered via the form.
    return redirect('/index')
  return render_template('login.html', title="Sign In", form=form)

@app.route('/licenses')
def licenses():
  return render_template('licenses.html')

