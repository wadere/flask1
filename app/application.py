'''
Simple Flask application to test deployment to Amazon Web Services
'''

from flask import Flask


application = Flask(__name__)

@application.route('/')
@application.route('/index')
def index():
    return "hello good man!"



if __name__ == '__main__':
    application.run(host='0.0.0.0', debug=True)
