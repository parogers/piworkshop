#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

ECHO = 2
TRIG = 3

GPIO.setmode(GPIO.BCM)
GPIO.setup(TRIG, GPIO.OUT)
GPIO.setup(ECHO, GPIO.IN)

GPIO.output(TRIG, False)
time.sleep(1)

while 1:
  # The module wants 10us to send the ultra-sonic pulses
  GPIO.output(TRIG, True)
  time.sleep(0.00001)
  GPIO.output(TRIG, False)

  # The module sends back a high pulse that times how long it took
  # to receive an ultrasound signal back. So wait until the ECHO
  # pin goes high (start of the pulse) and note the time.
  pulse_start = 0
  pulse_end = 0
  start = time.time()
  while not(GPIO.input(ECHO) and time.time()-start < 2):
    pulse_start = time.time()

  # Wait for the pulse to go low again
  while (GPIO.input(ECHO)):
    pulse_end = time.time()

  # Calculate the duration, and use that 
  pulse_duration = pulse_end - pulse_start
  distance = pulse_duration * 17150

  print "Distance: %0.1f cm" % distance

GPIO.cleanup()

