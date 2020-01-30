#!/usr/bin/python3
import RPi.GPIO as GPIO
import time
import sys

gpiomap = {"1" : 4,
           "2" : 17,
           "3" : 18,
           "4" : 27,
           "5" : 22,
           "6" : 23,
           "7" : 24,
           "8" : 10}

def init_gpios():
    # print("init GPIOs")
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    for idx in range (1,9):
        idx_temp = "{}".format(idx)
        GPIO.setup(gpiomap[idx_temp],GPIO.OUT)
    return

#def cleanup():
#    GPIO.cleanup()

def test_relais():
    print("test relais")
    for idx in range (1,3):
        GPIO.output(gpiomap["1"],True)
        time.sleep(1)
        GPIO.output(gpiomap["1"],False)
        GPIO.output(gpiomap["2"],True)
        time.sleep(1)
        GPIO.output(gpiomap["2"],False)
        GPIO.output(gpiomap["3"],True)
        time.sleep(1)
        GPIO.output(gpiomap["3"],False)
        GPIO.output(gpiomap["4"],True)
        time.sleep(1)
        GPIO.output(gpiomap["4"],False)
        GPIO.output(gpiomap["5"],True)
        time.sleep(1)
        GPIO.output(gpiomap["5"],False)
        GPIO.output(gpiomap["6"],True)
        time.sleep(1)
        GPIO.output(gpiomap["6"],False)
        GPIO.output(gpiomap["7"],True)
        time.sleep(1)
        GPIO.output(gpiomap["7"],False)
        GPIO.output(gpiomap["8"],True)
        time.sleep(1)
        GPIO.output(gpiomap["8"],False)
    return

def handle_request (relais, action):

    if relais not in ("1","2","3","4","5","6","7","8"):
        print("error: first parameter not valid")
        return

    if action not in ("on","off","toggle","read"):
        print("error: action not valid")
        return

    if action == "on":
        print("handle_request on{}".format(gpiomap[relais]))
        GPIO.output(gpiomap[relais],True)

    if action == "off":
        print("handle_request off{}".format(gpiomap[relais]))
        GPIO.output(gpiomap[relais],False)

    if action == "read":
        if GPIO.input(gpiomap[relais]) == 1:
            b = "on"
        else:
            b = "off"

        print ("relais", relais, "is", b)

    if action == "toggle":
        GPIO.output(gpiomap[relais],False)
        time.sleep(1)
        GPIO.output(gpiomap[relais],True)

    return

def usage():
    print("gpioctrl - switch relais on PDU")
    print("")
    print("example calls:")
    print("")
    print("  switch relais 5 on:")
    print("    gpioctrl 5 on")
    print("")
    print("  switch relais 1 off:")
    print("    gpioctrl 1 off")
    print("")
    print("  toggle relais 2")
    print("    gpioctrl 2 toggle")
    print("")
    print("  read status of relais 7")
    print("    gpioctrl 7 read")

if __name__=="__main__":
    init_gpios()
    if (len(sys.argv) == 2) and sys.argv[1] == "test":
        test_relais()
    elif (len(sys.argv) == 3):
        handle_request( sys.argv[1], sys.argv[2])
    else:
        print("invalid command")
        usage()
        
        
