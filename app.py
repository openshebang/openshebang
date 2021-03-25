from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
  pagename = "OpenShebang Home"
  username = 'Dion'
  companyname = 'uOnline'
  return render_template('index.html', pagename=pagename, username=username, companyname=companyname)
