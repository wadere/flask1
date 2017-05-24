from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.from_object('config')
app_settings = app.config['APP_SETTINGS']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wordcount_dev'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost/wordcount_dev'

db = SQLAlchemy(app)

from models import *

@app.route('/')
def hello():
    return "Hello using postgres and flask-sqlalchemy!"


@app.route('/')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
