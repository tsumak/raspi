import RPi.GPIO as GPIO
import time 
import os
GPIO.setmode(GPIO.BCM)

# shutdown pin
halt_pin = 21


# pullup
GPIO.setup(halt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

#while True:
#
#	GPIO.wait_for_edge(halt_pin, GPIO.FALLING)
#	print("yhdistetty")


def int_shutdown(halt_pin):
	#sammuta rpi
	print "sammutetaan!"
	os.system("sudo reboot")
	time.sleep(3)


# make halt_pin as interrupt input
# react to falling edge and call our interrupt "int_shutdown"
GPIO.add_event_detect(halt_pin, GPIO.FALLING, callback = int_shutdown, bouncetime = 5000)

# else sleep
while 1:
	time.sleep(1)
