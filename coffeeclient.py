#! /usr/bin/python

import urllib.request, urllib.error, urllib.parse
import traceback
import subprocess

SECRET = "233499"
URL = "http://guarded-reef-2427.herokuapp.com/coffee/long/" + SECRET

def alarm():
    subprocess.call("/etc/coffee/alarm.sh")

while 1:
    try:
        print(URL)
        resp = urllib.request.urlopen(URL)
        data = resp.read()
        print(data)
        if (data.find(b"COFFEE") > -1):
            alarm()
    except KeyboardInterrupt:
        break
    except:
        print("Exception, retrying: ")
        traceback.print_exc()



