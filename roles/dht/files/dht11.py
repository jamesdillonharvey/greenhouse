import argparse
import Adafruit_DHT
import time
 


parser = argparse.ArgumentParser()
parser.add_argument("-p", "--pin", type=int, help="pin number")
args = parser.parse_args()

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = args.pin


while True:
    humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
    if humidity is not None and temperature is not None:
        print("Temp={0:0.1f}C Humidity={1:0.1f}%".format(temperature, humidity))
    else:
        print("Sensor failure. Check wiring.");
    time.sleep(3);
