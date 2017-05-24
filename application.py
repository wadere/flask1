'''
Simple Flask application to test deployment to Amazon Web Services
Uses Elastic Beanstalk and RDS

Author: Scott Rodkey - rodkeyscott@gmail.com

Step-by-step tutorial: https://medium.com/@rodkey/deploying-a-flask-application-on-aws-a72daba6bb80
'''

from flask import Blueprint, render_template, request, Flask


application = Flask(__name__)

@main.route('books/')
def display_books():
    books= {
        'Learn Python the heard way': { 'author': "Shaw, Zed",
                                        'rating':'3.92'
                                        }
    }

if __name__ == '__main__':
    application.run(host='0.0.0.0')
