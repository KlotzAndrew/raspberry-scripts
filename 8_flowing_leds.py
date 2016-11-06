#! /usr/bin/env python
 
import RPi.GPIO as GPIO
import time

pins = [14, 15, 18, 17, 27, 22, 23, 24]

def setup():
    GPIO.setmode(GPIO.BCM)
    for pin in pins:
        GPIO.setup(pin, GPIO.OUT)
        GPIO.output(pin, GPIO.LOW)

def loop():
    while True:
        for pin in pins:
            GPIO.output(pin, GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(pin, GPIO.LOW)

def destroy():
    for pin in pins:
        GPIO.output(pin, GPIO.LOW)
    GPIO.cleanup()

if __name__ == '__main__':
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()

