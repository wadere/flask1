import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/wordcount_dev'

db = SQLAlchemy(app)


@app.route('/')
def hello():
    return "Hello World! with Postgresql and Flask-SQLAlchemy"

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run()