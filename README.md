# greenhouse

## Image

https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

```
lsblk -p


sudo umount /dev/sda1
sudo umount /dev/sda2

unzip -p raspios_lite_armhf_latest | sudo dd of=/dev/sda bs=4M status=progress conv=fsync


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
