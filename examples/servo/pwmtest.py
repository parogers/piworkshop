#!/usr/bin/env python

import time
from RPi import GPIO

channel = 2
period = 25
frequency = 1.0/(period/1000.0)

GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)
p = GPIO.PWM(channel, frequency)
p.start(2.5)

minDutyP = 0.5
maxDutyP = 2.5

def calc_duty(n):
	tm = minDutyP + n*(maxDutyP-minDutyP)
	return 100*tm / float(period)

p.ChangeDutyCycle(calc_duty(0))
time.sleep(2)
p.ChangeDutyCycle(calc_duty(1))
time.sleep(2)

#print calc_duty(1)

n = 0
while 1:
	break
	#p.ChangeDutyCycle(calc_duty(0))

	#for n in range(10):
	#	p.ChangeDutyCycle(calc_duty(n/10))
	#	time.sleep(1)

	print "DONE"

p.stop()

GPIO.cleanup()

