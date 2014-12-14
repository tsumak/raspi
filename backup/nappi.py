import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

# shutdown pin
halt_pin = 21

#temp
GPIO.setup(24, GPIO.OUT)
#temp


# pullup
GPIO.setup(halt_pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

while True:

	GPIO.wait_for_edge(halt_pin, GPIO.FALLING)

	print("yhdistetty")
	GPIO.output(24, True)
	time.sleep(3)
	GPIO.output(24, False)	
		

GPIO.cleanup()
