## kaksitoiminen nappi. (paina kerran = boot, pidä pohjassa = shutdown)

import RPi.GPIO as GPIO
import time, os

GPIO.setwarnings(False)

# pinout mapping BCM/BOARD
GPIO.setmode(GPIO.BCM)

# pin variables
pin = 21		# nappi
rele = 24		# rele out

# pullup/setup
GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)      # nappi
GPIO.setup(rele, GPIO.OUT)                              # rele out

# turn output ON to turn relay OFF (only for with this relay perkele)
GPIO.output(rele, True)

## done setting up ---------------------------------------------------

def nappi(pin):
	GPIO.remove_event_detect(pin)
	painettu = time.time() ; print "painettu"

	GPIO.wait_for_edge(pin, GPIO.RISING)
	irroitettu = time.time() ; print "irroitettu"

	tulos = irroitettu - painettu
	if tulos < 0.5:
		print "REBOOT"
		time.sleep(3)
		os.system(shutdown -r now)
	elif tulos > 0.5:
		print "SHUTDOWN"
		time.sleep(3)
		os.system(shutdown -h now)

GPIO.add_event_detect(pin, GPIO.FALLING, callback=nappi, bouncetime=300)

# keep script running/waiting for event
while True:
	time.sleep(1)
