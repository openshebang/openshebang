from app import app # The first `app` is the directory, the second is the `app` function inside of the `__init__.py`

@app.route('/') # This is a decorator.
@app.route('/index') # You can chain decorators.
def index():
    return "Hello World!"

