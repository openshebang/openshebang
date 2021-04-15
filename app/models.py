# This defines the database itself.

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login # This is the LoginManager
from hashlib import md5 

class User(UserMixin, db.Model): # also import here the UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)


    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self): # This prints the name of each row in the 'User' table.
        return 'User: {}'.format(self.username)

    def avatar(self, size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow) # `index=True`, is handig als je de datum in een volgorde wilt verkijgen. # de `datetime` moet nog geimporteerd worden
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Dit is in de 'user', tabel, de 'id' column
    
    def __repr__(self):
        return 'Post {}:'.format(self.body)

class F1Teams(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    teamname = db.Column(db.String(64), index=True, unique=True)
    team_afkorting = db.Column(db.String(3), unique=True)
    rijder_1 = db.Column(db.String(64))
    rijder_2 = db.Column(db.String(64))

    def __repr__(self):
        return 'F1Team'.format(self.teamname)

@login.user_loader
def load_user(id):
    return User.query.get(int(id)) # De `id` is een string dus moet een int worden.

class Articles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), index=True)
    subtitle = db.Column(db.String(), index=True)
    content = db.Column(db.String(), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Dit is in de 'user', tabel, de 'id' column
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)

    def __repr__(self):
        return 'Article: '.format(self.title)

class DibEntries(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(), index=True)
    content = db.Column(db.String(), index=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id')) # Dit is in de 'user', tabel, de 'id' column
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    image = db.Column(db.String())

    def __repr__(self):
        return 'Dib Entry: '.format(self.title)

class DibSettings(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    delay = db.Column(db.Integer, default=5000)
    toptext = db.Column(db.String())
    topimage = db.Column(db.String())
    url1 = db.Column(db.String())
    url2 = db.Column(db.String())
    url3 = db.Column(db.String())
    url4 = db.Column(db.String())
    url5 = db.Column(db.String())

    def __repr__(self):
        return 'DIB Settings: '.format(self.delay, self.toptext, self.topimage)

# Wordt onderstaande nog gebruikt !?!?
class DbImages(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return 'DB Image: '.format(self.name)