import RPi.GPIO as GPIO
import time
import numpy as np
import math as math
import matplotlib.pyplot as plt

GPIO.setmode(GPIO.BCM)
Ds = [26, 19, 13, 6, 5, 11, 9, 10] 
GPIO.setup(Ds, GPIO.OUT)


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

# def create_sin(f, sF, time) :
#     int size_arr = sF * time
#     arr = []
#     for i in range(0, size_arr) :
#         arr.attend() = math.sin(float(i * f))
#     return arr

def show_sin(amplitude, sF) :
    for i in amplitude:
        cur = int(round(i * 127) + 128)
        # print(cur)
        out = num2dac(cur)
        GPIO.output(Ds, out)
        time.sleep(float(1/ int(sF)))


freq = int(input('input frequency'))
sF = int(input('input sampling frequency'))
t = int(input('input time'))

tim = np.arange(0, t, float(1/sF)) 
amplitude = np.sin(tim*freq* 2 * math.pi)
plt.plot(tim, amplitude)
plt.title('Sin')
plt.xlabel('time')
plt.ylabel('amplitude sin(time)')
plt.show()   
show_sin(amplitude, sF)
GPIO.output(Ds, 0)
GPIO.cleanup() 