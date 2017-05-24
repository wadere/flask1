from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello you handsom devil you!"


@app.route('/')
def hello_name(name):
    return "Hello {}!".format(name)


if __name__ == '__main__':
    app.run()
