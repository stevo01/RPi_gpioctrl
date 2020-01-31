#!/usr/bin/python3
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO

gpiomap = {"/gpio/switch/1": 4,
           "/gpio/switch/2": 17,
           "/gpio/switch/3": 18,
           "/gpio/switch/4": 27,
           "/gpio/switch/5": 22,
           "/gpio/switch/6": 23,
           "/gpio/switch/7": 24,
           "/gpio/switch/8": 10}

msgmap = {b'1': True,
          b'0': False}


def init_gpios():
    # print("init GPIOs")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for idx in range(1, 9):
        idx_temp = "/gpio/switch/{}".format(idx)
        GPIO.setup(gpiomap[idx_temp], GPIO.OUT)
    return


# The callback for when the client receives a CONNACK response from the server.
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))

    # Subscribing in on_connect() means that if we lose the connection and
    # reconnect then subscriptions will be renewed.
    client.subscribe("/gpio/switch/1")
    client.subscribe("/gpio/switch/2")
    client.subscribe("/gpio/switch/3")
    client.subscribe("/gpio/switch/4")
    client.subscribe("/gpio/switch/5")
    client.subscribe("/gpio/switch/6")
    client.subscribe("/gpio/switch/7")
    client.subscribe("/gpio/switch/8")


# The callback for when a PUBLISH message is received from the server.
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))
    print("output port = {}, state = {}".format(gpiomap[msg.topic], msgmap[msg.payload]))
    GPIO.output(gpiomap[msg.topic], msgmap[msg.payload])


if __name__ == "__main__":
    print("mqtt_client started")
    init_gpios()
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect("localhost", 1883, 60)

    client.loop_forever()
    print("mqtt_client stopped")
    exit(0)
