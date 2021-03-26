from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
  pagename = "OpenShebang Home"
  username = 'Dion'
  companyname = 'uOnline'
  title = 'Hey er is een title!'
  return render_template('admin.html', pagename=pagename, username=username, companyname=companyname, title=title)

