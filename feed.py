#! /usr/bin/env python

import datetime, os, sys, codecs
from feedparser import parse

scriptPath  = os.path.dirname(sys.argv[0])

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


f = codecs.open(scriptPath+'/pages/studentposts.md', 'w', encoding='utf-8').write(output)
print scriptPath
print "All done!"
