import os
from feedparser import parse
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.flatpages import FlatPages


URLS = ['http://parezcoydigo.wordpress.com/feed', 'http://lawyersgunsmoneyblog.com/feed']
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
Bootstrap(app)
pages = FlatPages(app)


def get_feed(url):
    f=parse(url)
    return f

@app.route('/')
def index():
    return render_template('base.html')

@app.route('/studentposts/')
def posts(urls=URLS):
    feedList = {}
    for url in urls:
        feedList[url]=get_feed(url)
    return render_template('students.html', feedList=feedList)            
    
@app.route('/<path:path>/')
def page(path):
   page = pages.get_or_404(path)
   template = page.meta.get('extends', 'norm.html')
   return render_template(template, page=page)


if __name__ == '__main__':
    app.run(debug=True)
    
#   port = int(os.environ.get('PORT',5000))
#   app.run(host='0.0.0.0', port=port)

