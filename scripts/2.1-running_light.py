import RPi.GPIO as GPIO
import time as time

GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27,22, 10, 9]
GPIO.setup(leds , GPIO.OUT)

for j in range(10):   
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(1)
        GPIO.output(i, 0)
        time.sleep(0.1)
GPIO.output(leds, 0)
GPIO.cleanup()
