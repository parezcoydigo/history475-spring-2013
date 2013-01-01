#! /usr/bin/env python

import datetime, os
from feedparser import parse

scriptPath  = os.path.dirname(__file__)

urls=['http://parezcoydigo.wordpress.com/feed', 'https://americasouthandnorth.wordpress.com/feed/']
today = datetime.datetime.now()

def get_feed(url):
    return parse(url)

my_feeds = [ get_feed(urls[i]) for i in range(0,len(urls)) ]

output = '''extends: norm.html
title: Recent Student Posts
date: %d-%d-%d


''' % (today.year, today.month, today.day)


for feed in my_feeds:
    output = output + "### " + feed.feed.title + "\n*  " + "[" + feed.entries[0].title + "](" + feed.entries[0].link + ")-- "\
            + feed.entries[0].summary + "\n\n"


f = open(scriptPath+'/pages/studentposts.md', 'w').write(output)
print "All done!"
