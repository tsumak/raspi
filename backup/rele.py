import RPi.GPIO as GPIO
import time
import sys
GPIO.setmode(GPIO.BCM)

# set pin 24 as output
GPIO.setup(24, GPIO.OUT)

# and turn it ON (for relay to be off)
GPIO.output(24, True)

# wait 
time.sleep(1)

#while True:

for i in range(1):

	GPIO.output(24, True)
	time.sleep(1)

	GPIO.output(24, False)
	time.sleep(1)


GPIO.cleanup()


# quit without message
exit()
quit()

# quit with message
sys.exit("Valmis")
