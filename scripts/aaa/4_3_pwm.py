import RPi.GPIO as GPIO

import time as time

GPIO.setmode(GPIO.BCM)
GPIO.setup(24 , GPIO.OUT)
pin = GPIO.PWM(24, 100)
pin.start(0)
try:
    while True:
        try:
            koef = int(input())
            pin.ChangeDutyCycle(koef)
            time.sleep(1)
            print(3.3*koef/100)
        except ValueError:
            print('Введите целое неотрицательное число')
except KeyboardInterrupt:       
    pin.stop()
    GPIO.output(24, 0)
    GPIO.cleanup()