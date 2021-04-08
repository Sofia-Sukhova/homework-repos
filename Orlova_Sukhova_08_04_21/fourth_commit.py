import RPi.GPIO as GPIO
import time
import numpy as np
import math as math
import matplotlib.pyplot as plt
import scipy as sc



GPIO.setmode(GPIO.BCM)
Ds = [26, 19, 13, 6, 5, 11, 9, 10] 
GPIO.setup(Ds, GPIO.OUT)


sc.io.wavfile.read  ("SOUND.WAV")
