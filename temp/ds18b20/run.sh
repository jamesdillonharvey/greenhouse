#! /bin/bash
 
# Read Temperature
tempread=`cat /sys/bus/w1/devices/10-000802b4ba0e/w1_slave`
# Format
temp=`echo "scale=2; "\`echo ${tempread##*=}\`" / 1000" | bc`
 
# Output
echo "The measured temperature is " $temp "°C"
