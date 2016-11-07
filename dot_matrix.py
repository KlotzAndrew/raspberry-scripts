#! /usr/bin/env python

import RPi.GPIO as GPIO
import time

latch = 17
clock = 27
data = 22

code_H = [0x01,0xff,0x80,0xff,0x01,0x02,0x04,0x08,0x10,0x20,0x40,0x80,0xff,0xff,0xff,0xff,0xff,0xff,0xff,0xff]
code_L = [0x00,0x7f,0x00,0xfe,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0x00,0xfe,0xfd,0xfb,0xf7,0xef,0xdf,0xbf,0x7f]

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
    while True:
        for i in range(0, len(code_H)):
            hc595_in(code_L[i])
            hc595_in(code_H[i])
            hc595_out()
            time.sleep(0.1)

        for i in range(len(code_H)-1, -1, -1):
            hc595_in(code_L[i])
            hc595_in(code_H[i])
            hc595_out()
            time.sleep(0.1)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

