import RPi.GPIO as GPIO
import time


bin_depth = 8
def decToBinList(number):
    p = 0
    N = bin_depth - 1
    X = []
    while N > 0:
        p = int(number/ 2**N)
        if p == 1:
            X.append(1)
            number -= 2**N 
        else:
            X.append(0)
        N -= 1
    X.append(number)
    return X


GPIO.setmode(GPIO.BCM)
leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(leds, GPIO.OUT)
a = 21
b = 0
for i in range(0, 256):
    X = []
    X = decToBinList(i)

    for i in range(0, bin_depth):
        GPIO.output(leds[i], X[i])
    time.sleep(0.2)
    GPIO.output(leds, 0)
GPIO.cleanup()
