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
sudo apt-get install ansible -y

```

## Run ansible

```
ansible-playbook run.yaml


```


## DHT

From here : https://www.thegeekpub.com/236867/using-the-dht11-temperature-sensor-with-the-raspberry-pi/

### Add to ansible

```
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT
```


## logging for free?

https://io.adafruit.com/





