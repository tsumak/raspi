# hdmi pois/paalle pythonilla
import os
import sys

input = int(raw_input("hdmi paalle vai pois (1 tai 0): "))


if input == 1:
	os.system("sudo /opt/vc/bin/tvservice -p")

elif input == 0:
	os.system("sudo /opt/vc/bin/tvservice -o")

else:
	print "Vaara input"	

