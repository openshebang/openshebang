# openshebang/wsgi.py
# When a file in the main folder is called `app.py` or `wsgi.py` than it will automatically run, without specifying it.

from blog import app # Run with `flask --app openshebang --debug` # You can also `export FLASK_APP=microblog.py`



