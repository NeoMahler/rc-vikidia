# -*- coding: utf-8 -*-

import json
import web
import time
import re
import urllib2
import socket

rcchan = '#vikidia-recentchanges'

class MyException(Exception):
    pass

def rc_all(phenny, input, lang, lastrevids):
    global rcchan
    url = lang + u'.vikidia.org/w/api.php?action=query&list=recentchanges&rcprop=title|ids|user|comment&rclimit=1&rctype=edit|new&format=json'

    try:
        tmp = web.get(url)
    except socket.timeout, e:
        # For Python 2.7
        raise MyException("There was an error: %r" % e)
    # phenny.say("web.get(url) -> " + tmp)
    if len(tmp) == 0:
        return
    snippet = json.loads(tmp)

    changes = snippet['query']['recentchanges']
    
    if lang in lastrevids:
        changes = filter(lambda x: x['revid'] > lastrevids[lang], changes)
 
    if len(changes) == 0:
        return
    
    lastrevids[lang] = changes[0]['revid']
    
    vikidia_url = 'URL: http://%s.vikidia.org/wiki/' % lang
    def diff_url(diff, oldid):
        return 'Diff: http://%s.vikidia.org/w/index.php?title=&diff=%s&oldid=%s' % (lang, diff, oldid)
    
    for change in changes:
        print change
        parser = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
        searchResult = parser.search(change['user'])
        #phenny.say(searchResult)
            
        if change['type'] == 'new':
            if searchResult:
                phenny.msg(rcchan, u'[%s.vikidia] \x02IP\x02 %s \x02created\x02 %s - %s %s%s' % (lang, change['user'], change['title'], change['comment'], vikidia_url, change['title'].replace(' ', '_')))
            else:
                phenny.msg(rcchan, u'[%s.vikidia] \x02User\x02 %s \x02created\x02 %s - %s %s%s' % (lang, change['user'], change['title'], change['comment'], vikidia_url, change['title'].replace(' ', '_')))
        elif change['type'] == 'log':
            phenny.say('[%s.vikidia] Log action, performed by %s on the page %s.' % (lang, change['user'], change['title']))
        else:
            if searchResult:
                phenny.msg(rcchan, u'[%s.vikidia] \x02IP\x02 %s \x02edited\x02 %s - %s %s' % (lang, change['user'], change['title'], change['comment'], diff_url(change['revid'], change['old_revid'])))
            else:
                phenny.msg(rcchan, u'[%s.vikidia] \x02User\x02 %s \x02edited\x02 %s - %s %s' % (lang, change['user'], change['title'], change['comment'], diff_url(change['revid'], change['old_revid'])))

def autostart(phenny, input):
    if input.nick.startswith('rc-vikidia'):
        main(phenny, input)

autostart.event = ('JOIN')
autostart.rule = r'.*'

def start(phenny, input):
    main(phenny, input)

start.commands = ['start']

def main(phenny, input):
    lastrevids = {}
    while True: 
        rc_all(phenny, input, 'fr', lastrevids)
        rc_all(phenny, input, 'es', lastrevids)
        rc_all(phenny, input, 'it', lastrevids)
        rc_all(phenny, input, 'en', lastrevids)
##        rc_all(phenny, input, 'de', lastrevids)
##        rc_all(phenny, input, 'ru', lastrevids)
#        rc_all(phenny, inpuy, 'language code here', lasrevids)
	time.sleep(1)

