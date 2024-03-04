import RPi.GPIO as GPIO

import time as time
voltages = [3.25, 1.68, 0.87, 0.46, 0.11, 0.05]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setup(dac , GPIO.OUT)
GPIO.output(dac, number)
time.sleep(15)
GPIO.output(dac, 0)
GPIO.cleanup()