from app import app # From the `app`-folder, import the `app` instance
from app import db # Dit is nodig om onderstaande shell context
from app.models import User, Post

# Het onderste zorgt ervoor dat alle modellen worden toegevoegd aan de 'flask shell'.
@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Post': Post}
