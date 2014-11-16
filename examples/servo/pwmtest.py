#!/usr/bin/env python

import time
from RPi import GPIO

# Servo motors are controlled via a series of pulses (on/off) at a
# specific frequency. The length of time the pulse is on (compared
# to how long it's off) determines what angle the servo rotates to.

# The pin connected to the servo
channel = 2

# The period of the pulse (in milliseconds). This is standard for 
# most servo motors.
period = 25
# Calculate the frequency based on the period
frequency = 1.0/(period/1000.0)
# This is the minimum on time (in ms) for the pulse
minDutyP = 0.5
# This is the maximum on time
maxDutyP = 2.5

# Given a percentage, calculate the duty cycle needed to have the
# servo rotate to that position. Think of the full range of motion
# as being a number from 0 to 100. With zero being full rotation
# clockwise, and 100 being full rotation counter-clockwise.
def calc_duty(n):
	tm = minDutyP + n*(maxDutyP-minDutyP)/100.0
	return 100*tm / float(period)

# Setup the servo pin as an output
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.OUT)

# Start sending a PWM (pulse-width modulation) to the servo
p = GPIO.PWM(channel, frequency)
# This command starts the pulsing, given a duty cycle (on time)
p.start(calc_duty(0))

# Rotate the servo fully one way
p.ChangeDutyCycle(calc_duty(0))
time.sleep(2)

# Rotate the servo fully the opposite way
p.ChangeDutyCycle(calc_duty(100))
time.sleep(2)

# Rotate the servo to the mid point
p.ChangeDutyCycle(calc_duty(100))
time.sleep(2)

# Stop sending a PWM signal
p.stop()

GPIO.cleanup()
