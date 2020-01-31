# Overview
The project includes sample for access to RaspberryPi GPIO ports with MQTT protocol.

The current implementation allows you to control eight outputs of raspberry PI Board.
The following table shows the mapping of the PINS.

| number | GPIO Port on RaspberryPi  | comment  |
| ------ |:-------------:| -----:|
| 1      | 4             |  |
| 2      | 17            |  |
| 3      | 18            |  |
| 4      | 27            |  |
| 5      | 22            |  |
| 6      | 23            |  |
| 7      | 24            |  |
| 8      | 10            |  |


## install mqtt message broker and git on your raspberry pi

execute following commands tio install required software packages on your raspberry pi
```
sudo apt install mosquitto mosquitto-clients git python3 python-pip3
pip3 install paho-mqtt
```

## clone project and start application

execute following commands on your raspberry pi to clone the repository:
```
cd /home/pi
git clone https://github.com/stevo01/RPi_gpioctrl
```

execute following commands to start the mqtt client
```
cd /home/pi
python3 mqtt_client.py
```

## autostart
```
sudo chmod +x gpio_mqtt_client.sh
sudo cp gpio_mqtt_client.sh /etc/init.d/
systemctl daemon-reload
```

## test application with command line

### monitor all toppics on raspberry message broker
```
mosquitto_sub -h 192.168.1.80 -t /# -q 1
```

### switch first GPIO on and off
```
mosquitto_pub -h 192.168.1.80 -t /gpio/switch/1 -m '1'
sleep 1
mosquitto_pub -h 192.168.1.80 -t /gpio/switch/1 -m '0'
```

## control application with  MQTT dash (android implementation of MQTT client)

### Install and start Mqtt dash (from google app store)
see https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=de for further informations

### configure MQTT dash
t.b.d

## MQTT toppic description

the following table liste all used toppics and message content:

| toppic         | message       | comment                                           |
| -------------- |:-------------:| :------------------------------------------------:|
| /gpio/switch/1 | "0" or "1"    | "0" - set port 1 to low, "1" = set port 1 to high |
| /gpio/switch/2 | "0" or "1"    | "0" - set port 2 to low, "1" = set port 2 to high |
| /gpio/switch/3 | "0" or "1"    | "0" - set port 3 to low, "1" = set port 3 to high |
| /gpio/switch/4 | "0" or "1"    | "0" - set port 4 to low, "1" = set port 4 to high |
| /gpio/switch/5 | "0" or "1"    | "0" - set port 5 to low, "1" = set port 5 to high |
| /gpio/switch/6 | "0" or "1"    | "0" - set port 6 to low, "1" = set port 6 to high |
| /gpio/switch/7 | "0" or "1"    | "0" - set port 7 to low, "1" = set port 7 to high |
| /gpio/switch/8 | "0" or "1"    | "0" - set port 8 to low, "1" = set port 8 to high |

# Bookmarks
# https://play.google.com/store/apps/details?id=net.routix.mqttdash&hl=de for further info
# http://blog.scphillips.com/posts/2013/07/getting-a-python-script-to-run-in-the-background-as-a-service-on-boot/
