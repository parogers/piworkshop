#!/usr/bin/env python

import cgi
import traceback
import sys
import os

print "Content-type: text/html"
print ""
print "Hello world"

cwd = os.getcwd()
fifoPath = os.path.join(cwd, "..", "server", "comm")

try:
    args = cgi.FieldStorage()
    value = args.getvalue("def")
    if (value):
        open(fifoPath, "w").write(value)

except:
    traceback.print_exc(file=sys.stdout)

print "DONE"
