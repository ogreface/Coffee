#!/usr/bin/python
"""A web.py application powered by gevent"""

from gevent import monkey; monkey.patch_all()
from gevent.pywsgi import WSGIServer
from gevent.event import Event
import time
import web
import os

urls = ("/coffee/(\d+)", "index",
        '/coffee/long/(\d+)', 'long_polling')

FLAG=Event()
class index:
    def GET(self,id):
        global FLAG
        FLAG.set()
        FLAG.clear()
        return 'Alarm sent'


class long_polling:
    # Since gevent's WSGIServer executes each incoming connection in a separate greenlet
    # long running requests such as this one don't block one another;
    # and thanks to "monkey.patch_all()" statement at the top, thread-local storage used by web.ctx
    # becomes greenlet-local storage thus making requests isolated as they should be.
    def GET(self,id):
        global FLAG
        FLAG.wait()
        return 'COFFEE:'+ str(time.time())


if __name__ == "__main__":
    application = web.application(urls, globals()).wsgifunc()
    port = int(os.environ['PORT'])
    print 'Serving on ' + str(port) + '...'
    WSGIServer(('', port), application).serve_forever()
