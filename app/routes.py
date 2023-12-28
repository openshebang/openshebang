from app import app # The first 'app' is the app-Package represents with the dir 'app', in that is a 'app' variable in the __init__.py file.


@app.route('/') # This is a decorator, that conntect / to this function
@app.route('/index') # Second decorator
def index():
    return "Hello World!"
