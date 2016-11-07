#! /usr/bin/env python

import RPi.GPIO as GPIO

signalPin = 17

counter = 0

def count(ev=None):
    global counter
    counter += 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(signalPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.add_event_detect(signalPin, GPIO.RISING, callback=count)

def loop():
    while True:
        global counter
        print 'counter = %d' % counter

def destroy():
    GPIO.cleanup()


if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

