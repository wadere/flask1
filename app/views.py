import feedparser
from flask import Flask
from flask import render_template

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
    return render_template('template/home.html',
                           title=first_article.get('title'),
                           published=first_article.get('published'),
                           summary=first_article.get('summary'))


if __name__ == '__main__':
    app.run(debug=True)