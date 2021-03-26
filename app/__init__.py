from flask import Flask

app = Flask(__name__)

from app import routes # De routes is `app\routes.py`. Deze moet onderaan.

