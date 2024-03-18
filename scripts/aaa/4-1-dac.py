import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac , GPIO.OUT)


def dec_to_bin(number):
    return [int(el) for el in bin(number)[2:].zfill(8)]
try:
    while True:
        number = input('Введите целое положительное число меньше 255:    ')
        if number == 'q':
            break
        else:
            try:
                if type(number) == float:
                    number == 'y'
                else:
                    number = int(number)
                    GPIO.output(dac, dec_to_bin(number))
                    print(number*3.3/256.0)
            
            except Exception:
                if int(number) > 255:
                    print('Введите число меньше 256')
                    continue
                
                if number == 'н':
                    print('Введите целое числ')

                elif int(number) < 0:
                    print("Введите положительное число")
                    continue
                   

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()    