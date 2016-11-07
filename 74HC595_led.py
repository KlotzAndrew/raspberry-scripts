#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

latch = 17
clock = 27
data = 22

LED0 = [0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80]
LED1 = [0x01,0x03,0x07,0x0f,0x1f,0x3f,0x7f,0xff]
LED2 = [0x01,0x05,0x15,0x55,0xb5,0xf5,0xfb,0xff]
LED3 = [0x02,0x03,0x0b,0x0f,0x2f,0x3f,0xbf,0xff]

def setup():
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(latch, GPIO.OUT)
    GPIO.setup(clock, GPIO.OUT)
    GPIO.setup(data, GPIO.OUT)
    GPIO.setup(latch, GPIO.LOW)
    GPIO.setup(clock, GPIO.LOW)
    GPIO.setup(data, GPIO.LOW)

def hc595_in(value):
    for bit in range(0, 8):
        GPIO.output(latch, 0x80 & (value << bit))
        GPIO.output(data, GPIO.HIGH)
        time.sleep(0.001)
        GPIO.output(data, GPIO.LOW)

def hc595_out():
    GPIO.output(clock, GPIO.HIGH)
    time.sleep(0.001)
    GPIO.output(clock, GPIO.LOW)

def loop():
    WhichLeds = LED0
    sleeptime = 0.1
    while True:
        for i in range(0, len(WhichLeds)):
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)

        for i in range(len(WhichLeds)-1, -1, -1):
            hc595_in(WhichLeds[i])
            hc595_out()
            time.sleep(sleeptime)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

