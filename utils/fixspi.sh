#!/bin/bash

gpio -g mode 10 alt0
gpio -g mode 9 alt0
gpio -g mode 11 alt0
gpio -g mode 8 output
gpio -g write 8 1
gpio -g mode 7 output
