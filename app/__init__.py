from flask import Flask # Import Flask
from config import Config # Needed below, for the SECRET_KEY

app = Flask(__name__) # Store that 'Flask' in a variable called 'app'
app.config.from_object(Config) # This is the 'Config' from the config.py file # Need to be imported (see above)
from app import routes # `app` is the folder, routes is the Module from routes.py # It is in the bottor to prevent 'circular dependancies'




