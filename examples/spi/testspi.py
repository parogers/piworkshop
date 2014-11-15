#!/usr/bin/python

import spi

status = spi.openSPI(speed=1000000)
print "SPI:", status

for x in range(16):
    data = spi.transfer((x,))
    print data[0]

spi.closeSPI()
