# .env (P.009)

So you don't have to set `EXPORT FLASK_APP=...` accross terminal sessions.

`)$ python3 -m pip install python-dotenv

Then create at the top lever a `.flaskenv`-file with the content: `FLASK_APP=openshebang.py`.

# git

Undo changes in a signle file `git checkout -- file.txt`

# WTF

`)$ pip install flask-wtf`

It is better to put config like this in a separate `config.py`-file:
`app.config['SECRET_KEY'] = 'hashhash'`

`<form action="" method="post" novalidate>` The `action` is send this to the same page., the novalidate is no validation and let Flask do the validation.

# Databases

`python3 -m pip install flask-sqlalchemy`
`python3 -m pip install flask-migrate`

Maak een database:
$ `flask db init` # This will create a `migrations` folder.

Bereid wijzigingen voor
$ `flask db migrate -m "Maak een tabel genaamd: users"`

Voor de wijzigingen daadwerkelijk voor:
$ `flask db upgrade`

SQLAlchemy gebruikt een snake-case. Dus een AdresEnTelefoon Classe wordt een adres_en_telefoon table.

Terugdraaien van een database upgrdade:

$ `flask db downgrade`

# Flask shell

fromwerkzeug.securityimportgenerate_password_hash, check_password_hash

`)$ python3 -m pip install flask-login

4 required items:

1. is_authenticated
2. is_active
3. is_anonymous (if this is True, than the user is NOT logged in)
4. get_id() this returns a string.

`python3 -m pip install email-validator`


