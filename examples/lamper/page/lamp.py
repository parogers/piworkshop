#!/usr/bin/env python

import cgi
import traceback
import sys
import os

print "Content-type: text/html"
print ""

# Get a path to the FIFO buffer (that will let us 
# communicate with the python server script)
cwd = os.getcwd()
fifoPath = os.path.join(cwd, "..", "server", "comm")

try:
    # Parse the URL arguments (eg localhost/lamper/page/lamp.py?cmd=...)
    args = cgi.FieldStorage()
    value = args.getvalue("cmd")
    if (value):
        # Send the command to the server
        open(fifoPath, "w").write(value)

except:
    traceback.print_exc(file=sys.stdout)

print """<html>
<body>

<a href="lamp.py?cmd=turn-on">Turn on light</a><br/>
<a href="lamp.py?cmd=turn-off">Turn off light</a><br/>
<a href="lamp.py?cmd=toggle">Toggle light</a><br/>

</body>
</html>
"""

