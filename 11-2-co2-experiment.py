import RPi.GPIO as GPIO

import time
import datetime

import numpy as np
import matplotlib.pyplot as plt

import co2Functions as func

leds = [21, 20, 16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]

bits = len(dac)
levels = 2 ** bits
dV = 3.3 / levels

comparator = 4 
troykaVoltage = 17
dinPin = 2

func.initGPIOco2()       

try: 
    for i in range (25):
        GPIO.output(dinPin, 1)
        time.sleep(0.0004)
        GPIO.output(dinPin, 0)
        time.sleep(0.0004)

finally:
    func.deinitGPIOco2()