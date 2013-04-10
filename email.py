#!/usr/bin/env python
import urllib2
import base64
import os
from xml.dom import minidom
from subprocess import call

username = ""
password = ""

try:
    request = urllib2.Request("https://mail.google.com/mail/feed/atom")
    base64string = base64.encodestring('%s:%s' % (username, password))\
                         .replace('\n', '')
    request.add_header("Authorization", "Basic %s" % base64string)
    result = urllib2.urlopen(request)
except:
    #Probably network error
    exit()
parsed = minidom.parseString(result.read())

titles = parsed.getElementsByTagName("title")
senders = parsed.getElementsByTagName("name")

if len(titles) <= 1:
    exit()
else:
    total = len(titles) - 1
    messages = {"total": total}
    for i in xrange(1, total + 1):
        messages[i] = dict(
            sender=senders[i-1].firstChild.nodeValue,
            subject=titles[i].firstChild.nodeValue)
        title = "%d unread %s" % (total, "mails" if total > 1 else "mail")
    body = []
    for i in xrange(1, total + 1):
        body.append(
            "Subject : %s \n\tFrom : %s" % (messages[i]["subject"], messages[i]["sender"]))
    call(["notify-send", title, "\n".join(body)])
