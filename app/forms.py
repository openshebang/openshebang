from flask_wtf import FlaskForm # all flask extenstions start with `flask_`
from wtforms import StringField, PasswordField, BooleanField, SubmitField # These fields are not provioded by Flask, so import them via wtformsa
from wtforms.validators import DataRequired

class LoginForm(FlaskForm): # All fields below have to be imported
    username = StringField('Username', validators=[DataRequired()]) # The 'Username' is the label for the HTML view
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')