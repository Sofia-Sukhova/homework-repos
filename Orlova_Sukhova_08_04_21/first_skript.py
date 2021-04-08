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

value = int(input('input a value'))

while value != -1: 
    out = []
    out = num2dac(value)
    # print (value, out)
    GPIO.output(Ds, out)
    value = int(input())
GPIO.cleanup()