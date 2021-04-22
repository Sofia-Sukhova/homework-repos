 
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
sig = 17
comp = 4
GPIO.setup(sig, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)

GPIO.output(sig, 1)

#first script adc
# value = 1
# while value != -1 : 
#     value = int(input('Enter a value(-1 to exit)>'))
#     out = []
#     out = num2dac(value)
#     # print (value, out)
#     GPIO.output(Ds, out)
#     volt = 3.3 * float (value) / 255  
#     print(value, "= %.2f" % volt, 'V')


# #second script adc
# while True:
#     value = 0
#     out = []
#     out = num2dac(value)
#     GPIO.output(Ds, out)
#     time.sleep(0.01)
#     while (GPIO.input (comp)) and (value < 255):
#         out = num2dac(value)
#         GPIO.output(Ds, out)
#         value += 1
#         time.sleep(0.0001)
#     volt = 3.3 * float (value) / 255 
#     print("Digital value: %d, Analog value: %.2f V" % (value, volt) )

# #third script adc
# while True:
#     value = 127
#     l = 0
#     r = 255
#     out = []
#     out = num2dac(value)
#     GPIO.output(Ds, out)
#     time.sleep(0.001)
#     cm = GPIO.input (comp)
#     while (r - l) > 1:
#         if cm == 0:
#             r = value
#         else:
#             l = value
#         value = int((l + r) / 2)
#         out = num2dac(value)
#         GPIO.output(Ds, out)
#         time.sleep(0.001)
#         cm = GPIO.input (comp)
#     volt = 3.3 * float (value) / 255 
#     print("Digital value: %d, Analog value: %.2f V" % (value, volt) )

#fouth script adc

def bin_find():
    value = 127
    l = 0
    r = 255
    out = []
    out = num2dac(value)
    GPIO.output(Ds, out)
    time.sleep(0.001)
    cm = GPIO.input (comp)
    while (r - l) > 1:
        if cm == 0:
            r = value
        else:
            l = value
        value = int((l + r) / 2)
        out = num2dac(value)
        GPIO.output(Ds, out)
        time.sleep(0.001)
        cm = GPIO.input (comp)
    volt = 3.3 * float (value) / 255 
    return value

def number_of_lights(val):
    n = int(round(val * 8 / 255))
    return (n)

LEDS = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setup(LEDS, GPIO.OUT)

while True:
    val = bin_find()
    n = number_of_lights(val)
    out = []
    n = (1 << n) - 1
    out = num2dac(n)
    GPIO.output(LEDS, out)
    time.sleep(0.001)
GPIO.cleanup()
