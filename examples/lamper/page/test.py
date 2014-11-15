#!/usr/bin/env python

import time
import cgi
import traceback
import sys
import os

print "Content-type: text/plain"
print ""

cwd = os.getcwd()
fifoPath = os.path.join(cwd, "..", "server", "comm")

try:
    for n in range(5):
        sys.stdout.write("Hello world\n")
        sys.stdout.flush()
        time.sleep(1)

except:
    traceback.print_exc(file=sys.stdout)
