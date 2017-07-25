import feedparser
import os
from flask import Flask
from flask import render_template
from flask import request
import json, urllib2, urllib

import jinja2
jinja_environment = jinja2.Environment(autoescape=True,loader=jinja2.FileSystemLoader(os.path.join(os.path.dirname(__file__), 'templates')))

app = Flask(__name__, template_folder='template/')

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'cnn': 'http://rss.cnn.com/rss/edition.rss',
             'fox': 'http://feeds.foxnews.com/foxnews/latest'}

DEFAULTS = {'publication':'bbc',
            'city':'London, UK',
            'currency_from': 'GBP',
            'currency_to':'USD'}

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=60ff7feffe4519e5fae6666312880962'
CURRENCY_URL = "https://openexchangerates.org//api/latest.json?app_id=32671043335d465f8c425d5d4f3791b4"

@app.route('/')
@app.route('/<publication>')
def home():
    # do work for the articles
    publication=request.args.get("publication")
    if not publication:
        publication=DEFAULTS['publication']
    articles = get_news(publication)

    # do work for the city weather
    city = request.args.get('city')
    if not city:
        city = DEFAULTS['city']
    weather=get_weather(city)

    # setup the to and from currency then get conversions
    currency_from = request.args.get('currency_from')
    if not currency_from:
        currency_from = DEFAULTS['currency_from']
    currency_to = request.args.get('currency_to')
    if not currency_to:
        currency_to = DEFAULTS['currency_to']
    rate, currencies = get_rate(currency_from,currency_to)

    return render_template('home.html', articles=articles, weather=weather, source=publication.upper(),
                           currency_from=currency_from, currency_to=currency_to, rate=rate)



def get_news(query):
    if not query or query.lower() not in RSS_FEEDS:
        publication=DEFAULTS['publication']
    else:
        publication = query.lower()
    feed = feedparser.parse(RSS_FEEDS[publication])
    return feed['entries']


def get_weather(query):
    api_url=WEATHER_URL
    query = urllib2.quote(query)
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

def get_rate(frm, to):
    all_currency = urllib2.urlopen(CURRENCY_URL).read()
    parsed = json.loads(all_currency).get('rates')
    frm_rate=parsed.get(frm.upper())
    to_rate=parsed.get(to.upper())
    return (to_rate/frm_rate, parsed.keys())

if __name__ == '__main__':
    app.run(debug=True)