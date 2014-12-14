# testi kaksoistoimiselle napille
# painallus ja pohjassa pito ovat eri toimintoja

import RPi.GPIO as GPIO
import time

debug = 0	# debug variable
GPIO.setwarnings(False)


if debug == 1:
	GPIO.cleanup()
	

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


# define funktiot
def rele_kerran():               # funktio 1x
        GPIO.output(rele, False)
        time.sleep(1)
        GPIO.output(rele, True)
	time.sleep(1)	

def rele_monta():                # funktio 3x
        for i in range(3):

                GPIO.output(rele, False)
		time.sleep(1)

		GPIO.output(rele, True)
		time.sleep(1)

def nappi(pin):
	while True:
		print "nappi painettu (FALLING) - reboot"
		painettu = time.time()
		GPIO.wait_for_edge(pin, GPIO_RISING)
		irroitettu = time.time()
	
		tulos = irroitettu - painettu

		if tulos <= 2:
			print "tulos on alle 2"
		elif tulos > 5:
			print "tulos on yli 2"

##debug
if debug == 1:
	print "testataan funktio kerran"
	rele_kerran()
	print "kerta toimii"

	time.sleep(3)
	print "entas kolme kertaa.."

	rele_monta()
	print "montakin toimii"


	print "valmis. funktiot ok!"
	GPIO.cleanup()		
	exit()
## eod

GPIO.add_event_detect(pin, GPIO.FALLING, callback=nappi, bouncetime=300)

#while True:
#	
#	GPIO.wait_for_edge(pin, GPIO.FALLING)
#	painettu = time.time()
#
#	GPIO.wait_for_edge(pin, GPIO.RISING)
#	irroitettu = time.time()
#
#	# debug
#	print "tulos on: ",
#	print irroitettu - painettu

while True:
	time.sleep(1)

GPIO.cleanup()



