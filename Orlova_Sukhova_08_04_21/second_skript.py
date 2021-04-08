import RPi.GPIO as GPIO
import time

bin_depth = 8
def num2dac(value):
    p = 0
    N = bin_depth - 1
    X = []
    while N > 0:
        p = int(value/ 2**N)
        if p == 1:
            X.append(1)
            value -= 2**N 
        else:
            X.append(0)
        N -= 1
    X.append(value)
    return X

GPIO.setmode(GPIO.BCM)
Ds = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(Ds, GPIO.OUT)

def repetitionsNumber():
    for i in range(0, 255):
        out = num2dac(i)
        GPIO.output(Ds, out)
        time.sleep(0.01)
    while i > -1:
        out = num2dac(i)
        GPIO.output(Ds, out)
        time.sleep(0.01)
        i -= 1 


repNumber = int(input('input a repetition Number  '))
i = repNumber
GPIO.output(Ds, 0)
while i  > 0: 
    repetitionsNumber()
    i -= 1
GPIO.output(Ds, 0)
GPIO.cleanup()