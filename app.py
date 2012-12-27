import os
from feedparser import parse
from flask import Flask, render_template
from flask.ext.bootstrap import Bootstrap
from flask.ext.markdown import Markdown

app = Flask(__name__)
Bootstrap(app)
Markdown(app)

URLS = ['http://parezcoydigo.wordpress.com/feed', 'http://lawyersgunsmoneyblog.com/feed']

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
    
if __name__ == '__main__':
#    app.run(debug=True)
    port = int(os.environ.get('PORT',5000))
    app.run(host='0.0.0.0', port=port)

