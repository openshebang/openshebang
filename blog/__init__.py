from flask import Flask
from config import Config # The first 'config' is the `config.py`, the second `Config` is the defined class inside that file.

app = Flask(__name__)
app.config.from_object(Config) # See the above import. # To test this in the CLI: $ python3 >>> from blog import app >>> app.config['SECRET_KEY'] # This will return the challenge. # In the OS you can also do first 'export SECRET_KEY='dummy from OS'.

from blog import routes # This have to be in the bottom to avoid Flask circular dependancies
