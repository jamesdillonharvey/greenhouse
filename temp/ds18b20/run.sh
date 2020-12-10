#! /bin/bash
 
while true; do 
# Read Temperature
tempread=`cat /sys/bus/w1/devices/28-01191c92e270/w1_slave`
# Format
temp=`echo "scale=2; "\`echo ${tempread##*=}\`" / 1000" | bc`
 
# Output
echo "The measured temperature is " $temp "°C"
sleep 5
done
