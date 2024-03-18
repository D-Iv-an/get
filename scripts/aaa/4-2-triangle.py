import RPi.GPIO as GPIO

import time as time
def dec_to_bin(number):
    return [int(el) for el in bin(number)[2:].zfill(8)]
dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac , GPIO.OUT)
p = float(input())/510
while True:
    try:
        for i in range(256):
            GPIO.output(dac, dec_to_bin(i))
            time.sleep(p)
        for i in range(256):
            GPIO.output(dac, dec_to_bin(255 - i))
            time.sleep(p)

    except KeyboardInterrupt:
        GPIO.output(dac, 0)
        GPIO.cleanup()

