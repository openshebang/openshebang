import os

from flask import Flask

def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping( # De config wordt automatisch doorgegeven aan een template
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'osb.sqlite'),
        WEBSITE_NAME="OpenOnderwijs", # Deze is om de standaard 'flaskr' naam te kunnen veranderen. Dit is ook in de Template aangepast
        SHOW_REGISTER_AND_LOG_IN=False, # Deze is om de 'Register' en 'Log In' naam al dan niet te tonen, want deze is niet altijd wensbaar.
    )


    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # a simple page that says hello
    @app.route('/hello')
    def hello():
        return 'Hello, World!'

    from . import db
    db.init_app(app)
 
    from . import auth
    app.register_blueprint(auth.bp)

    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app