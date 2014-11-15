#!/usr/bin/python

import time
import RPi
from RPi import GPIO

LED_PIN = 2

# Set BCM numbering for the pins
GPIO.setmode(GPIO.BCM)
# Setup the LED pin as an output
GPIO.setup(LED_PIN, GPIO.OUT)

# Turn the LED on
GPIO.output(LED_PIN, 1)
time.sleep(1)
# Turn it off again
GPIO.output(LED_PIN, 0)
time.sleep(0)

GPIO.cleanup()
