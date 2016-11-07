#! /usr/bin/env python

import RPi.GPIO as GPIO
import time


latch = 17
clock = 27
data = 22

segCode = [0x3f,0x06,0x5b,0x4f,0x66,0x6d,0x7d,0x07,0x7f,0x6f,0x77,0x7c,0x39,0x5e,0x79,0x71,0x80]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(latch, GPIO.OUT)
    GPIO.setup(clock, GPIO.OUT)
    GPIO.setup(data, GPIO.OUT)
    GPIO.setup(latch, GPIO.LOW)
    GPIO.setup(clock, GPIO.LOW)
    GPIO.setup(data, GPIO.LOW)

def hc595_shift(value):
    for bit in range(0, 8):
        GPIO.output(latch, 0x80 & (value << bit))
        GPIO.output(data, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(data, GPIO.LOW)
    GPIO.output(clock, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(clock, GPIO.LOW)

def loop():
    while True:
        for i in range(0, len(segCode)):
            print 'i is %d' % i
            hc595_shift(segCode[i])
            time.sleep(0.5)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

