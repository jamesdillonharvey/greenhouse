

from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

set_temp = 75;

try:
    while true:
        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "01191c92e270")
        temp = sensor.get_temperature()
        print("water temp %.2c target temp %.2c" % (temp, set_temp))

        if temp < set_temp:
            GPIO.output(5, GPIO.LOW)
            print("ON")
        else:
            GPIO.output(5, GPIO.HIGH)
            print("OFF")


        if temp >= set_temp:
        set_temp = 65
        print("PHASE 2")
except:
    GPIO.output(5, GPIO.HIGH)
    print("TURN OFF ERROR")
