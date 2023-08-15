from flask import Flask

app = Flask(__name__)

from blog import routes # This have to be in the bottom to avoid Flask circular dependancies
