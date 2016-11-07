#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

outputA = 17
outputB = 27
button_pin = 22

counter = 0

flag = 0
bLastState = 0
bState = 0

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(outputA, GPIO.IN)
    GPIO.setup(outputB, GPIO.IN)
    GPIO.setup(button_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    rotaryClear()

def rotaryDeal():
    global flag
    global bLastState
    global bState
    global counter
    bLastState = GPIO.input(outputB)
    while(not GPIO.input(outputB)):
        bState = GPIO.input(outputB)
        flag = 1
    if flag == 1:
        flag = 0
        if (bLastState == 0) and (bState == 1):
            counter += 1
            print 'counter = %d' % counter
        if (bLastState == 1) and (bState == 0):
            counter -= 1
            print 'counter = %d' % counter

def clear(ev=None):
    global counter
    counter = 0
    print 'counter = %d' % counter

def rotaryClear():
    GPIO.add_event_detect(button_pin, GPIO.FALLING, callback=clear, bouncetime=200)

def loop():
    global counter
    while True:
        rotaryDeal()

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

