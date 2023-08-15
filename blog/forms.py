from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField # You have to import the functions from wtforms.
from wtforms.validators import DataRequired # To make it mandatory to fill this in.

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()]) # The argument is going to be the label of the form or the button in HTML.
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')