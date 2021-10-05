import RPi.GPIO as GPIO
import time
def dectobin(v, r):
    return [int(bit) for bit in bin(v)[2:].zfill(r)]
def dectodtac(v,r,dac):
    sig = dectobin(v,r)
    GPIO.output(dac, sig)
    time.sleep(0.1)
    return sig

leds =  [ 21, 20, 16, 12, 7, 8, 25, 24 ]
dac = [ 26, 19, 13, 6, 5, 11, 9, 10 ]
aux = [ 22,23,27,18,15,14,3,2]

mV = 3.3
bits = len(dac)
raz = 2**bits

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(22, GPIO.OUT, initial = GPIO.LOW)
p1 = GPIO.PWM(22, 1000)
try:
    while 0==0:
        print("Please write a number for duty cycle")
        check = False
        inputS = input()
        if inputS.isdigit():
            dc = int(inputS)
            if dc < 0:
                print('incorrect value, enter a postitive number')
            elif dc >100:
                print('incorect value, enter a number less pr equal to 100')
            else:
                if check == False:
                    p1.start(dc)
                    check = True
                else: 
                    p1.ChangeDutyCycle(dc)
            
        else:
            if inputS == 'qu':
                break
            else:
                print("Please, enter a number")
except KeyboardInterrupt:
    print("program was interupted from keyboard")
else:
    print("no exceptions happened")
finally:
    p1.stop()
    GPIO.output(dac, GPIO.LOW)
    GPIO.output(22, GPIO.LOW)
    GPIO.cleanup(dac)
    
    print("done, GPIO cleaned up")

