#! /usr/bin/env python

import RPi.GPIO as GPIO

LedPin = 17
BtnPin = 27  

Led_status = 1

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LedPin, GPIO.OUT)
    GPIO.setup(BtnPin, GPIO.IN, pull_up_down=GPIO.PUD_UP)
    GPIO.output(LedPin, GPIO.HIGH)

def switch_led(ev=None):
    global Led_status
    Led_status = not Led_status
    GPIO.output(LedPin, Led_status)
    if Led_status == 1:
        print 'led off...'
    else:
        print '...led on'

def loop():
    GPIO.add_event_detect(BtnPin, GPIO.FALLING, callback=switch_led, bouncetime=200)
    while True:
        pass

def destroy():
    GPIO.output(LedPin, GPIO.HIGH)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()
 
