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
SECRET=233499
class index:
    def GET(self,passedId):
        global FLAG
        global SECRET
        print passedId
        id = int(passedId)
        if (id == SECRET):
            FLAG.set()
            FLAG.clear()
            return 'Alarm sent'
        else:
            return "Invalid secret"


class long_polling:
    # Since gevent's WSGIServer executes each incoming connection in a separate greenlet
    # long running requests such as this one don't block one another;
    # and thanks to "monkey.patch_all()" statement at the top, thread-local storage used by web.ctx
    # becomes greenlet-local storage thus making requests isolated as they should be.
    def GET(self,passedId):
        global FLAG
        global SECRET
        id = int(passedId)
        if (id == SECRET):
            FLAG.wait()
            return 'COFFEE:'+ str(time.time())
        else:
            return "Invalid Secret"


if __name__ == "__main__":
    application = web.application(urls, globals()).wsgifunc()
    port = int(os.environ['PORT'])
    print 'Serving on ' + str(port) + '...'
    WSGIServer(('', port), application).serve_forever()
