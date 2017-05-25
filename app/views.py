import feedparser
import os
from flask import Flask
from flask import render_template
from flask import request
import json, urllib2, urllib

import jinja2
jinja_environment = jinja2.Environment(autoescape=True,
    loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

app = Flask(__name__, template_folder='template/')

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'}

DEFAULTS = {'publication':'bbc',
            'city':'London, UK'}

@app.route('/')
@app.route('/<publication>')
def home():
    publication=request.args.get("publication")
    if not publication:
        publication=DEFAULTS['publication']
    articles = get_news(publication)
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather=get_weather(city)
    return render_template('home.html', articles=articles, weather=weather, source=publication.upper())



def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication=DEFAULTS['publication']
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']


def get_weather(query):
    api_url='http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=60ff7feffe4519e5fae6666312880962'
    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get('weather'):
        weather= {'description':parsed['weather'][0]['description'],
                  'temparature':parsed['main']['temp'],
                  'city':parsed['name'],
                  'country':parsed['sys']['country']
                  }
        return weather


if __name__ == '__main__':
    app.run(debug=True)