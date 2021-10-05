import RPi.GPIO as GPIO
import time
leds = [21, 20 ,16, 12, 7, 8, 25, 24]
dac = [26, 19, 13, 6, 5, 11, 9, 10]
bits = len(dac)
levels = 2**bits
maxvolt = 3.3
troykaModule = 17
comp = 4

def decimal2binary(decimal):
    return [int(bit) for bit in bin(decimal)[2:].zfill(bits)]

def bin2dac(value):
    signal = decimal2binary(value)  
    GPIO.output(dac, signal)      
    return signal

def indificator(voltage):
    p = int((voltage/maxvolt)*10)
    sig = int(2**(p-1) - 0.5)

def adc(a,b):
    if (b-a > 1):
        signal = bin2dac(int(a + int((b-a)/2)))
        time.sleep(0.0007)
        compvalue = GPIO.input(comp)
        if (compvalue == 0):
            adc(a, a + int((b-a)/2))
        else:  adc(a + int((b-a)/2), b)
    else:
        signal = bin2dac(int(a + int((b-a)/2)))
        voltage = (a/levels)*maxvolt
        indificator(voltage)
        print("ADC value = {:3} -> {}, output voltage = {:.2f}".format(a, signal, voltage))
            
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(troykaModule, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)




try:
    while True:
        adc(0,256)

except KeyboardInterrupt:
    print("The program was stoped by the keyboard")
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup(dac)
    print("GPIO cleanup completed")
