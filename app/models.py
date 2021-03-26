# This defines the database itself.

from app import db
from datetime import datetime
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
from flask_login import UserMixin
from app import login # This is the LoginManager

class User(UserMixin, db.Model): # also import here the UserMixin
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self): # This prints the name of each row in the 'User' table.
        return 'User: {}'.format(self.username)

class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body=db.Column(db.String(140))
    timestamp=db.Column(db.DateTime, index=True, default=datetime.utcnow) # `index=True`, is handig als je de datum in een volgorde wilt verkijgen. # de `datetime` moet nog geimporteerd worden
    user_id=db.Column(db.Integer, db.ForeignKey('user.id')) # Dit is in de 'user', tabel, de 'id' column
    
    def __repr__(self):
        return'Post {}:'.format(self.body)

@login.user_loader
def load_user(id):
    return User.query.get(int(id)) # De `id` is een string dus moet een int worden.