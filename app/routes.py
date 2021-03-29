from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from app import app
from app import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import EditProfileForm
from app.forms import ArticleForm
from app.models import User
from app.models import F1Teams # Nu kan je met de data uit de database werken.
from app.models import Articles
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required # Dit is voor de decoratr @app.required
from werkzeug.urls import url_parse
from datetime import datetime

@app.before_request # This applies to any request, so you only have to write this once.
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow() # This will be a long datetime string
    db.session.commit()


@app.route('/')
@app.route('/index')
@login_required
def index():
  pagename = "OpenShebang Home"
  username = 'Dion'
  companyname = 'uOnline'
  title = 'Hey er is een title!'
  variables = {
    'username' : 'Dion Dresschers',
  }
  posts = [
    {
        'author' : {'username':'Dion'},
        'body' : "Dit is een tekst",
    },
    {
        'author' : {'username':'Jip'},
        'body' : "Dit is de tweede test",
    },
  ]
  return render_template('admin.html', pagename=pagename, companyname=companyname, title=title, posts=posts)

@app.route('/login', methods=['GET', 'POST'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = LoginForm()
  if form.validate_on_submit(): # If the submit button has been pushed and it is succesful.
    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data): # the last is the password check
      flash('Invalid username or password')
      return redirect(url_for('login'))
    login_user(user, remember=form.remember_me.data)
    next_page = request.args.get('next') # Voor zaken als `/login?next=/index`
    if not next_page or url_parse(next_page).netloc !='': # Als er bijvoorbeeld naar example.com geredirect wilt laten worden
      next_page = url_for('index')
    return redirect(next_page)
    flash('Login requested for user {}, remember_me={}'.format(form.username.data, form.remember_me.data))
  return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
  logout_user()
  return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('index'))
  form = RegistrationForm()
  if form.validate_on_submit():
    user = User(username=form.username.data, email=form.email.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash('You are now a new registered user!')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@app.route('/f1')
def f1():
  teams = F1Teams.query.all()
  return render_template('f1.html', teams=teams)

@app.route('/user/<username>')
@login_required
def user(username):
  user = User.query.filter_by(username=username).first_or_404() # A 404 error message will be sent if the user is not found in the database.
  posts = [
    {'author': user, 'body': 'Test post # 1'},
    {'author': user, 'body': 'Test post # 2'},
    {'author': user, 'body': 'Test post # 3'},
  ]
  return render_template('user.html', user=user, posts=posts)

@app.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile(): # we geven de username door voor de usernamecheck niet dubbel 
  form = EditProfileForm(current_user.username)
  if form.validate_on_submit():
    current_user.username = form.username.data # The latter is the data that is entered in the html form by the user.
    current_user.about_me = form.about_me.data # The latter is the data that is entered in the html form by the user.
    db.session.commit()
    flash('Your changes has been submitted')
    return redirect(url_for('edit_profile'))
  # This will propagate all the information form the existing database
  elif request.method == 'GET': # This is a 'GET'-method, so when the user wants to view the info
    form.username.data = current_user.username # Note that this is the excact opposite of above `current_user.username = form.username.data`
    form.about_me.data = current_user.about_me
  return render_template('edit_profile.html', title='Edit Profile', form=form)

@app.route('/article/new', methods=['GET','POST'])
@login_required
def article_new():
  form = ArticleForm()
  if form.validate_on_submit():
    article = Articles(title=form.title.data, content=form.content.data, user_id=current_user.username) # De `Articles zit in de models.py`
    db.session.add(article)
    db.session.commit()
    flash('Your post has been created!')
    return redirect(url_for('index'))
  return render_template('create_article.html', title='New Article', form=form)

@app.route('/blog')
def blog():
  articles = Articles.query.all()
  return render_template('blog.html', articles=articles)