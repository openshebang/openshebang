from flask import render_template
from app import app # This is for the used decorator.
from app import db # This is for the db rollback.

@app.errorhandler(404)
def not_found_error(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def internal_error(error):
    db.session.rollback() # it is best with an error, not to save this error to the database. The db.session.rollback() is the opposit of db.session.commit(), and it will rollback befor the database session has opened.
    return render_template('500.html'), 500