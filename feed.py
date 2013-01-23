#! /usr/bin/env python

import datetime, os, sys, codecs
from feedparser import parse

scriptPath  = os.path.dirname(sys.argv[0])

urls=['http://parezcoydigo.wordpress.com/feed', 'http://rockytopranger.wordpress.com/feed', 'http://cbbucs09.wordpress.com/feed', 'http://athenasowl1.wordpress.com/feed', 'http://willpatterson1.wordpress.com/feed', 'http://moconn475.wordpress.com/feed','http://cshinklesr2013.wordpress.com/feed','http://nsprouse.wordpress.com/feed','http://mesohistoryblog.wordpress.com/feed','http://gohomecolonistsyouredrunk.wordpress.com/feed','http://gorillawarfare475.wordpress.com/feed','http://ecraig3.wordpress.com/feed','http://dymer3.wordpress.com/feed','http://igotoseekagreatperhaps1.wordpress.com/feed','http://mjones56.wordpress.com/feed','http://fantasmadecipactli.wordpress.com/feed','http://annawgreene.wordpress.com/feed','http://lasindigenas.wordpress.com/feed','http://mmcginn7.wordpress.com/feed','http://jrpoole92590.wordpress.com/feed','http://jperugin.wordpress.com/feed']

today = datetime.datetime.now()

def get_feed(url):
    return parse(url)

my_feeds = [ get_feed(urls[i]) for i in range(0,len(urls)) ]

output = '''extends: norm.html
title: Recent Student Posts
date: %d-%d-%d


''' % (today.year, today.month, today.day)


for feed in my_feeds:
    try:
        output = output + "### " + feed.feed.title + "\n*  " + "[" + feed.entries[0].title + "](" + feed.entries[0].link + ")-- "+ feed.entries[0].summary + "\n\n"
    except IndexError:
        continue


f = codecs.open(scriptPath+'pages/studentposts.md', 'w', encoding='utf-8').write(output)
print scriptPath
print "All done!"
