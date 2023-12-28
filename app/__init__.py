from flask import Flask # Import Flask

app = Flask(__name__) # Store that 'Flask' in a variable called 'app'

from app import routes # `app` is the folder, routes is the Module from routes.py # It is in the bottor to prevent 'circular dependancies'




