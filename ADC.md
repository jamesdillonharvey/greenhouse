## stuff

https://learn.adafruit.com/adafruit-pcf8591-adc-dac/python-circuitpython

https://daycounter.com/Calculators/Voltage-Divider-Calculator.phtml

# note
External Voltage source needs to connect to ground of the board also.


# history

```
  366  sudo pip3 install adafruit-circuitpython-pcf8591
  367  vim adc.py
  368  python3 adc.py 
  369  vim /etc/modprobe.d/raspi-blacklist.conf
  370  sudo vim /etc/modprobe.d/raspi-blacklist.conf
  371  sudo vim /etc/modules
  372  modprobe i2c-dev
  373  lsmod
  374  python3 adc.py 
  375  ValueError: No Hardware I2C on (scl,sda)=(3, 2)
  376  ic2detect
  377  vim adc.py 
  378  ls /dev/i2c* /dev/spi*
  379  sudo apt-get install -y python-smbus
  380  sudo apt-get install -y i2c-tools
  381  sudo raspi-config 
  382  ls /dev/i2c* /dev/spi*
```

# code

```
# SPDX-License-Identifier: MIT
import time
import board
 
import adafruit_pcf8591.pcf8591 as PCF
from adafruit_pcf8591.analog_in import AnalogIn
from adafruit_pcf8591.analog_out import AnalogOut
 
############# AnalogOut & AnalogIn Example ##########################
#
# This example shows how to use the included AnalogIn and AnalogOut
# classes to set the internal DAC to output a voltage and then measure
# it with the first ADC channel.
#
# Wiring:
# Connect the DAC output to the first ADC channel, in addition to the
# normal power and I2C connections
#
#####################################################################
i2c = board.I2C()
pcf = PCF.PCF8591(i2c)
 
pcf_in_0 = AnalogIn(pcf, PCF.A0)
#pcf_out = AnalogOut(pcf, PCF.OUT)
 
while True:
 
    raw_value = pcf_in_0.value
    ref_value = pcf_in_0.reference_voltage
    print("raw Pin 0: %0.2f" % (raw_value))
    print("scale Pin 0: %0.2fV" % (ref_value))
    scaled_value = (raw_value / 65535) * pcf_in_0.reference_voltage
    print("scale Pin 0: %0.2fV" % (scaled_value))
    print("")
    time.sleep(3)
 
 ```
