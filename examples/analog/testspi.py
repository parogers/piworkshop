#!/usr/bin/python

import spi
import RPi
from RPi import GPIO

RST_PIN = 8
ENABLE_PIN = 7

status = spi.openSPI(speed=500000, mode=1)

GPIO.setmode(GPIO.BCM)

GPIO.setup(ENABLE_PIN, GPIO.OUT)
GPIO.output(ENABLE_PIN, 1)

for n in range(4):
	a = spi.transfer((44,))
	b = spi.transfer((66,))
	print a[0], b[0]

print ""

GPIO.output(ENABLE_PIN, 0)
GPIO.cleanup()

spi.closeSPI()

