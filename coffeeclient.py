#! /usr/bin/python

import urllib2
import traceback
import subprocess

SECRET = "233499"
URL = "http://guarded-reef-2427.herokuapp.com/coffee/long/" + SECRET

def alarm():
    subprocess.call("./alarm.sh")

while 1:
    try:
        print URL
        resp = urllib2.urlopen(URL)
        data = resp.read()
        print data
        if (data.find("COFFEE") > -1):
            alarm()
    except KeyboardInterrupt:
        break
    except:
        print "Exception, retrying: "
        traceback.print_exc()



