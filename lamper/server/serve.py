#!/usr/bin/env python

import os
import sys
import select
import traceback

from lamp import Lamp

# The FIFO buffer that will receive commands for controlling the lamp
fifoPath = "comm"

#tmp = open(fifoPath, "w")
#print "HERE"

def main():
    lamp = Lamp()

    while 1:
        # Open the buffer and wait for somebody to send data
        fd = open(fifoPath)

        #(rlist, wlist, xlist) = select.select([fd], [], [])
        #print rlist

        for cmd in fd.readlines():
            # Process the command (strip off excess whitespace)
            cmd = cmd.strip()
            if (cmd == "turn-on"):
                lamp.set_on(True)
            elif (cmd == "turn-off"):
                lamp.set_on(False)
            elif (cmd == "toggle"):
                lamp.set_on(not lamp.state)

try:
    main()
except:
    traceback.print_exc()

