import RPi.GPIO as GPIO
import time

bin_depth = 8

def lightUp(ledNumber, period):
    GPIO.setmode(GPIO.BCM)
    leds = [24, 25, 8, 7, 12, 16, 20, 21]
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds[ledNumber], 1)
    time.sleep(period)
    GPIO.output(leds, 0)
    GPIO.cleanup()


def blink(ledNumber, blinkCount, blinkPeriod):
    GPIO.setmode(GPIO.BCM)
    leds = [24, 25, 8, 7, 12, 16, 20, 21]
    GPIO.setup(leds, GPIO.OUT)
    for i in range(0, blinkCount):
        GPIO.output(leds[ledNumber], 1)
        time.sleep(blinkPeriod)
        GPIO.output(leds[ledNumber], 0)
        time.sleep(blinkPeriod)
    GPIO.cleanup()

def runningLight(count, period):
    GPIO.setmode(GPIO.BCM)
    leds = [24, 25, 8, 7, 12, 16, 20, 21]
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, 0)
    for i in range(0, count):
        n = i % 8
        GPIO.output(leds[n], 1)
        time.sleep(period)
        GPIO.output(leds[n], 0)
    GPIO.cleanup()

def runningDark(count, period):
    GPIO.setmode(GPIO.BCM)
    leds = [24, 25, 8, 7, 12, 16, 20, 21]
    GPIO.setup(leds, GPIO.OUT)
    GPIO.output(leds, 1)
    for i in range(0, count):
        n = i % 8
        GPIO.output(leds[n], 0)
        time.sleep(period)
        GPIO.output(leds[n], 1)
    GPIO.cleanup()

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


def lightNumber(number):
    GPIO.setmode(GPIO.BCM)
    leds = [24, 25, 8, 7, 12, 16, 20, 21]
    GPIO.setup(leds, GPIO.OUT)
    # GPIO.output(leds, 0)
    x = []
    x = decToBinList(number)
    for i in range(0, bin_depth):
        GPIO.output(leds[i], x[bin_depth - 1 - i])
    time.sleep(0.5)
    GPIO.output(leds, 0)
    GPIO.cleanup()

def runningPattern(pattern, direction):
    GPIO.setmode(GPIO.BCM)
    leds = [24, 25, 8, 7, 12, 16, 20, 21]
    GPIO.setup(leds, GPIO.OUT)
    lightNumber(pattern)
    if direction > 0:
        while True:
            pattern = (pattern << 1) % 256 + int((pattern << 1) / 256)
            # print (pattern)
            lightNumber(pattern)
    else:
        i = 1
        while True:
            pattern = int(pattern / 2) + (pattern % 2) * 128
            # print (pattern)
            lightNumber(pattern)
    GPIO.output(leds, 0)
    GPIO.cleanup()



# 
runningPattern(34, 1)

