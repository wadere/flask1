import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'
             }

@app.route('/')
@app.route('/<publication>')
def get_news(publication='bbc'):
    feed = feedparser.parse(RSS_FEEDS[publication])

    first_article = feed['entries'][1]
    return """<html>
            <body>
                <h1> {3} Most Recent </h1>
                <b>{0}</br>
                <i>{1}</br>
                <p>{2}</br>
            </body>
            </html>""".format(first_article.get("title"),
                              first_article.get('published'),
                              first_article.get('summary'),
                              publication.upper())


if __name__ == '__main__':
    app.run(debug=True)