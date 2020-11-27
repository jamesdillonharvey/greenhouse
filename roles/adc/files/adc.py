# SPDX-FileCopyrightText: Copyright (c) 2020 Bryan Siepert for Adafruit Industries
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
 
# reading at 30v with 10k, 1k and 220 Resistiors 
scale_voltage = 46/65280
 
while True:
   
    raw_value = pcf_in_0.value
    print("raw Pin 0: %0.2f" % (raw_value))
    scaled_value = (raw_value * scale_voltage)
    print("scale Pin 0: %0.2fV" % (scaled_value))
    time.sleep(3)
 

