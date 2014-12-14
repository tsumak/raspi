## releen naksuttelu (käänteinen)
## rele päälle = input LOW
## rele pois   = input HIGH
import RPi.GPIO as GPIO
import time


## define function with name: ledBlink()
def ledBlink(pin, xmaara, delay):
	for i in range(xmaara):
		print "Iteration " + str(i+1)	# print loop
		GPIO.output(pin, False)		# pin HIGH
		time.sleep(delay)		# wait delay
		GPIO.output(pin, True)		# pin LOW
		time.sleep(0.4)			# wait for naks
	print "Valmis"			# loop valmis


# user input
pin = raw_input("Mika pinni? (24): ");
xmaara = raw_input("Monta kertaa naksutellaan: ");
delay = raw_input("Viive?: ");

GPIO.setmode(GPIO.BCM)
GPIO.setup(int(pin), GPIO.OUT)	# GPIO to output

# Kutsu funktio
ledBlink(int(pin), int(xmaara), float(delay))


GPIO.cleanup()
quit()


