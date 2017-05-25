import feedparser
import os
from flask import Flask
from flask import render_template

import jinja2
jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

app = Flask(__name__, template_folder='template/')

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'
             }

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])
    first_article = feed['entries'][0]
    return render_template('home.html',
                           articles=feed['entries'],source=publication.upper())


if __name__ == '__main__':
    app.run(debug=True)