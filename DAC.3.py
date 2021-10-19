import matplotlib.pyplot as plt 
import RPi.GPIO as GPIO
import time
import math

dac = [26, 19, 13, 6, 5, 11, 9, 10] 
leds = [21, 20, 16, 12, 7, 8, 25, 24] 
bits = len(dac)
levels = 2**bits
maxVoltage = 3.3
TroykaMoudle = 17
comparator = 4
adcData = [] #Файл с данными с АЦП

GPIO.setmode(GPIO.BCM) 
GPIO.setup(dac + leds, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(TroykaMoudle, GPIO.OUT, initial = GPIO.HIGH)
GPIO.setup(comparator, GPIO.IN)

def decimal2binary(i): 
    return [int(elem) for elem in bin(i)[2:].zfill(bits)]

def bin2dac(i): #функция отображения числа на панели dac
    signal = decimal2binary(i)
    GPIO.output(dac, signal)
    return signal

def adc(): #функция, которая с помощью побитового сдвига находит значение на компараторе
    value = 0
    for i in range(7, -1, -1):
        bin2dac(value + 2 ** i)
        time.sleep(0.0008)
        comparatorValue = GPIO.input(comparator)
        if comparatorValue == 1:
           value += 2 ** i
    return value

try:
    chek = True
    GPIO.output(TroykaMoudle, 1) #Подаем питание на тройку-модуль
    start = time.time() #Засекаем начало эксперимента
    print('Началась зарядка конденсатора.')
    while True:
        value = adc() #Считываем аналоговый сигнал с конденсатора
        GPIO.output(leds, decimal2binary(value)) #Отображаем значение value на панели leds
        if value >= 245 and chek: #Если зарядились, то отключаем питание
            GPIO.output(17, 0)
            print('Началась разрядка конденастора')
            chek = False
        if chek == False and value <= 1:
            adcData.append(value) #Если зарядились, то заканчиваем эксперимент
            end = time.time() #засекаем конец эксперимента
            T = round((end - start)/(len(adcData)-1), 5) #Считаем период
            ny = round(1/T, 5) #Считаем частоту
            break
        adcData.append(value) #Добавляем значение в список всех аналоговых значений
        voltage = maxVoltage / levels * value #Считаем напряжение
        print("digital value = {:^3}, analog VOLTAGE = {:.2f}".format(value, voltage))

    plt.plot(adcData) #Строим график
    with open('data.txt', 'w') as f1: #Создаем и заполняем файл data.txt
        for i in range(len(adcData)):
            f1.write(str(adcData[i]) + '\n')
    with open('settings.txt', 'w') as f2: #Создаем и заполняем файл settings.txt
        f2.write('T = ' + str(T) + '\n')
        f2.write('Ny = '+ str(ny) +'\n')
        f2.write('Шаг напряжения = ')
        f2.write(str(3.3/255))

    plt.show() #Выводим график

except KeyboardInterrupt:
    print("Прервано")
finally:
    GPIO.output(dac + leds, GPIO.LOW) #Обнуляем подачу напряжения
    GPIO.cleanup(dac)