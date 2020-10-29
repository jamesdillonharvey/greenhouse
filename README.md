# greenhouse

## Image

https://www.raspberrypi.org/documentation/installation/installing-images/linux.md

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
