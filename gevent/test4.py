# -*- coding: utf-8 -*-

from gevent import monkey; monkey.patch_all()
import gevent
import requests
from datetime import datetime


def f(url):
    print ("time: %s, GET: %s".format(datetime.now(), url))
    resp = requests.get(url)
    print ("time: %s, %d bytes received from %s.").format(datetime.now(), len(resp.text), url)


gevent.joinall([
        gevent.spawn(f, "https://www.python.org/"),
        gevent.spawn(f, "https://www.yahoo.com/"),
        gevent.spawn(f, "https://github.com/"),
])