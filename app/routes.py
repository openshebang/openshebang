from flask import render_template
from flask import flash
from flask import redirect
from flask import url_for
from flask import request
from flask import abort
from app import app
from app import db
from app.forms import LoginForm
from app.forms import RegistrationForm
from app.forms import EditProfileForm
from app.forms import ArticleForm
from app.forms import DibForm
from app.forms import DibSettingsForm
from app.models import User
from app.models import F1Teams # Nu kan je met de data uit de database werken.
from app.models import Articles
from app.models import DibEntries # Deze zit in de models.py
from app.models import DibSettings
from flask_login import current_user
from flask_login import login_user
from flask_login import logout_user
from flask_login import login_required # Dit is voor de decoratr @app.required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename # Voor het uploaden van files met een check...
from datetime import datetime
import imghdr # needed for the by us created function `validate_image`
from flask import send_from_directory # Necessary if NOT is send from the 'static' folder.
import os # Is this alreay done in the app.py !?


@app.before_request # This applies to any request, so you only have to write this once.
def before_request():
  if current_user.is_authenticated:
    current_user.last_seen = datetime.utcnow() # This will be a long datetime string
    db.session.commit()

@app.route('/admin')
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
@login_required
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
    article = Articles(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data, user_id=current_user.username) # De `Articles zit in de models.py`
    db.session.add(article)
    db.session.commit()
    flash('Your post has been created!')
    return redirect(url_for('index'))
  return render_template('create_article.html', title='New Article', form=form)

@app.route('/') # Dit rendert de mooie view
def blog_index():
  articles = Articles.query.all() # This grabs all articles from the database.
  return render_template('blog_index.html', articles=articles)

@app.route('/blog/articles') # Dit rendert een view in de Admin
@login_required
def blog_articles():
  articles = Articles.query.all() # This grabs all articles from the database.
  return render_template('blog_articles.html', articles=articles)

@app.route('/blog/article/update/<int:article_id>', methods=['POST','GET']) # Deze <article_id>  bestaat nog niet.
@login_required
def blog_article_update(article_id):
  article = Articles.query.get_or_404(article_id)
  if article.user_id != current_user.username:
    abort(403)
  form = ArticleForm()
  if form.validate_on_submit():
    article.title = form.title.data
    article.subtitle = form.subtitle.data 
    article.content = form.content.data
    # db.session.add(entry) # We don't have to 'add' something new to the database.
    db.session.commit()
    flash('Your Article has been updated!', 'succes')
    return redirect(url_for('blog_article', article_id=article.id))
  elif request.method == 'GET':
    form.title.data = article.title
    form.subtitle.data = article.subtitle
    form.content.data = article.content
  return render_template('create_article.html', form=form, article=article)

@app.route('/blog/article/<int:article_id>') #S Deze <article_id>  bestaat nog niet. # Dit is de backend-view voor het article.S
def blog_article(article_id):
  article = Articles.query.get_or_404(article_id)
  return render_template('blog_post.html', article=article)
 
@app.route('/blog_about')
def blog_about():
  return render_template('blog_about.html')

@app.route('/blog_contact')
def blog_contact():
  return render_template('blog_contact.html')

@app.route('/blog_add_post', methods=['GET','POST'])
@login_required
def blog_add_post():
  form = ArticleForm()
  if form.validate_on_submit():
    article = Articles(title=form.title.data, subtitle=form.subtitle.data, content=form.content.data, user_id=current_user.username) # De `Articles zit in de models.py`
    db.session.add(article)
    db.session.commit()
    flash('Your post has been created!')
    return redirect(url_for('blog_index'))
  return render_template('blog_add_post.html', form=form)

@app.route('/blog/<int:id>')
@login_required
def article(id):
  article = Articles.query.get_or_404(id) # Also only .query.get(id) exists
  return render_template('blog_article.html')


# DIB ------------------------------------------------------------------------------------
@app.route('/dib/new', methods=['GET','POST'])
@login_required
def dib_new():
  form = DibForm()
  if form.validate_on_submit():
    entry = DibEntries(title=form.title.data, content=form.content.data, image=form.image.data, user_id=current_user.username)
    db.session.add(entry)
    db.session.commit()
    flash('Your post has been created!')
    return redirect(url_for('index'))
  return render_template('dib_new.html', form=form)

@app.route('/dib/entries')
def dib_entries():
  entries = DibEntries.query.all()
  return render_template('dib_entries.html', entries=entries)

@app.route('/dib/entry/<int:entry_id>') # Deze <article_id>  bestaat nog niet.
def dib_entry(entry_id):
  entry = DibEntries.query.get_or_404(entry_id)
  return render_template('dib_entry.html', entry=entry)

@app.route('/dib/entry/update/<int:entry_id>', methods=['POST','GET']) # Deze <article_id>  bestaat nog niet.
@login_required
def dib_update_entry(entry_id):
  entry = DibEntries.query.get_or_404(entry_id)
  if entry.user_id != current_user.username:
    abort(403)
  form = DibForm()
  if form.validate_on_submit():
    entry.title = form.title.data 
    entry.content = form.content.data
    entry.image = form.image.data
    # db.session.add(entry) # We don't have to 'add' something new to the database.
    db.session.commit()
    flash('Your post has been updated!')
    return redirect(url_for('dib_entry', entry_id=entry.id))
  elif request.method == 'GET':
    form.title.data = entry.title
    form.content.data = entry.content
    form.image.data = entry.image
  return render_template('dib_new.html', form=form, entry=entry)

@app.route("/dib/entry/delete/<int:entry_id>", methods=['POST'])
@login_required
def dib_delete_entry(entry_id):
  entry = DibEntries.query.get_or_404(entry_id)
  if entry.user_id != current_user.username:
    abort(403)
  db.session.delete(entry)
  db.session.commit()
  flash('Your entry has been deleted.', 'danger')
  return redirect(url_for('index'))

@app.route('/dib/index')
def dib_index():
  entries = DibEntries.query.all()
  settings = DibSettings.query.get(1)
  urls = []
  urls.append('http://info.cern.ch/hypertext')
  urls.append('http://info.cern.ch/hypertext/WWW/TheProject.html')
  return render_template('dib_index.html', settings=settings, urls=urls, entries=entries)

@app.route('/dib/settings', methods=['POST', 'GET'])
def dib_settings():
  form = DibSettingsForm()
  if DibSettings.query.get(1):
    dib_settings = DibSettings.query.get(1)
  else:
    dib_settings = DibSettings(id=1, delay=5000, toptext='Nieuws', topimage='bla2.svg')
    db.session.add(dib_settings)
    db.session.commit()
  if form.validate_on_submit():
    dib_settings.delay = form.delay.data
    dib_settings.toptext = form.toptext.data
    dib_settings.topimage = form.topimage.data
    dib_settings.url1 = form.url1.data
    dib_settings.url2 = form.url2.data
    dib_settings.url3 = form.url3.data
    dib_settings.url4 = form.url4.data
    dib_settings.url5 = form.url5.data
    # db.session.add(dib_settings)
    db.session.commit()
    flash('This has been updated!', 'warning')
    return redirect(url_for('index'))
  if request.method == 'GET':
    form.delay.data = dib_settings.delay
    form.toptext.data = dib_settings.toptext
    form.topimage.data = dib_settings.topimage
    form.url1.data = dib_settings.url1
    form.url2.data = dib_settings.url2
    form.url3.data = dib_settings.url3
    form.url4.data = dib_settings.url4
    form.url5.data = dib_settings.url5
  return render_template('dib_settings.html', form=form)  

@app.route('/dib/entry/presentation/<int:entry_id>') # Deze <article_id>  bestaat nog niet.
def dib_entry_presentation(entry_id):
  entry = DibEntries.query.get_or_404(entry_id)
  settings = DibSettings.query.get(1)
  return render_template('dib_entry_presentation.html', entry=entry, settings=settings)

# /DIB

# Uploads ---------------------------------------------------------------------

# Here no decorator as this is NO route
def validate_image(stream):
    header = stream.read(512)
    stream.seek(0) 
    format = imghdr.what(None, header)
    if not format:
        return None
    return '.' + (format if format != 'jpeg' else 'jpg')

@app.route('/uploads/new') # If the request is a 'GET', otherwise see the 'POST', below...
def uploads_new_get():
    return render_template('uploads_new.html')

@app.route('/uploads/new', methods=['POST'])
def uploads_new_post():
  if request.method == 'POST':
    uploaded_file = request.files['file']
    filename = secure_filename(uploaded_file.filename)
    if filename != '':
        file_ext = os.path.splitext(filename)[1]
        if file_ext not in app.config['UPLOAD_EXTENSIONS'] or \
                file_ext != validate_image(uploaded_file.stream):
            abort(400)
        uploaded_file.save(os.path.join(app.config['UPLOAD_PATH'], filename))
  return render_template('uploads_new.html')

@app.route('/uploads/show')
def uploads_show():
  files = os.listdir(app.config['UPLOAD_PATH'])
  return render_template('uploads_show.html', files=files)

#@app.route('/uploads/<filename>')
#def upload(filename): 
#    return send_from_directory(app.config['UPLOAD_PATH'], filename)

# Cards -----------------------------------------------------------------------

@app.route('/cards/show_card')
def cards_show_card():
    suit = ['c', 'd', 'h', 's']

    def new_deck():
      deck = []
      for suitcard in suit:
          for rank in range (1, 14, +1):
              card = [suitcard, rank]
              deck.append(card)
      return deck

    def shuffle_deck(deck):
        from random import shuffle
        shuffle(deck)
        return deck
  
    def image_card(card):
      return card[0] + '-' + str(card[1]) + '.svg'
   
    deck = new_deck()
    deck = shuffle_deck(deck)

    def deal_top_card(deck):
        card = deck.pop(0) 
        return card

    card = deal_top_card(deck)   

    card = '/svg/cards/' + image_card(card) 

    return render_template('cards_show_card.html', card=card)

