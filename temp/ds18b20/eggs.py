from w1thermsensor import W1ThermSensor
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(5, GPIO.OUT)

set_temp = 30;

try:
    print("1")
    while True:
        sensor = W1ThermSensor(W1ThermSensor.THERM_SENSOR_DS18B20, "01191c92e270")
        temp = sensor.get_temperature()
        print("water temp {0} target temp {1}".format(temp,set_temp))

        if temp < set_temp:
            GPIO.output(5, GPIO.LOW)
            print("ON")
        else:
            GPIO.output(5, GPIO.HIGH)
            print("OFF")

        if temp >= set_temp:
            set_temp = 25
            print("PHASE 2")

        time.sleep(5)

except Exception as e:
    print(e)    
    GPIO.output(5, GPIO.HIGH)
    print("TURN OFF ERROR")

finally:
    print("clean up")
    GPIO.output(5, GPIO.HIGH)
    GPIO.cleanup() # cleanup all GPIO
    
