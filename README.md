# greenhouse

## Image

https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

```
lsblk -p


sudo umount /dev/sda1
sudo umount /dev/sda2

unzip raspios_lite_armhf_latest
sudo dd if=2020-08-20-raspios-buster-armhf-lite.img of=/dev/sda bs=4M status=progress conv=fsync

sudo mount /dev/sda1 /media/pi/

cd /media/pi/

sudo touch ssh

sudo vim wpa_supplicant.conf

sudo sync

cd ..

sudo umount /dev/sda1

```



```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=GB

network={
 ssid=""
 psk=""
}

```

## Log and manual setup
```
sudo /sbin/ifconfig wlan0 mtu 1036
sudo /etc/init.d/networking restart
sudo apt-get install git -y
git clone https://github.com/jamesdillonharvey/greenhouse.git

```

## install ansible
```



```

## Run ansible

```



```




start from scratch

## start

`sudo apt upgrade`

## greenhouse wifi

`/etc/rc.local`

```

sleep 30
iwconfig wlan0 power off

exit 0

```



```

sudo crontab -e

*/5 * * * * /bin/ping -q -c60 192.168.0.1 > /dev/null 2>&1 || (/sbin/ifdown --force wlan0 ;/sbin/ifup wlan0 ;/usr/bin/logger wifi on wlan0 restarted via crontab)

sudo crontab -l

```


## logging for free?

https://io.adafruit.com/



## 30 10 2020

```
sudo apt-get update
sudo apt-get install python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel

pip3 install adafruit-circuitpython-dht

sudo apt-get install libgpiod2

sudo apt-get install vim

adding the following line at the end of /etc/ssh/sshd_config

IPQoS cs0 cs0

ruled out my freeze/disconnection SSH problems :slight_smile:

Edit: explaination of the problem:
OpenSSH sets the TOS (type Of Service) field in the IP datagram as “lowdelay” for interactive sessions and “throughput” for non-interactive sessions. My router doesn’t handle properly those settings, so I changed them in Cs0, Cs0 (aka 0x00, 0x00) <==> (best effort, best effort) and solved the instability/freeze SSH issues.
Reference:
sshd_config(5) man page 133
Differentiated services 46
I’ll mark this post as solved after some days of testing.




https://learn.adafruit.com/dht-humidity-sensing-on-raspberry-pi-with-gdocs-logging/python-setup


import time
import board
import adafruit_dht
 
# Initial the dht device, with data pin connected to:
dhtDevice = adafruit_dht.DHT22(board.D4)
 
# you can pass DHT22 use_pulseio=False if you wouldn't like to use pulseio.
# This may be necessary on a Linux single board computer like the Raspberry Pi,
# but it will not work in CircuitPython.
# dhtDevice = adafruit_dht.DHT22(board.D18, use_pulseio=False)
 
while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
 
    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error:
        dhtDevice.exit()
        raise error
 
    time.sleep(2.0)
```


## connection issue

cant run top or vim

change mtu size

```
   36  ifconfig
   37  sudo /sbin/ifconfig wlan0 mtu 1036
   38  sudo /etc/init.d/networking restart
   39  ifconfig

```
