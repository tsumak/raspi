# Anturien lukeminen tiedostoon
# Luetaan anturit 10s valein tiedostoon 'arvot'
# /etc/rc.local kaynnistaa skriptin bootissa
#
# Kytkenta
# Rus	= 3.3V
# SiVa	= Signaali (GPIO4)
# Sin	= Gnd
# Ylosveto 3.3V - Signaali
#

import time

while True:

	# open files for read
	tempfile1 = open("/sys/bus/w1/devices/28-0000021ebfb4/w1_slave")
	tempfile2 = open("/sys/bus/w1/devices/28-000005fef4d4/w1_slave")
	tempfile3 = open("/sys/bus/w1/devices/28-000005ff61d6/w1_slave")

	# save files to variables
	data1 = tempfile1.read()
	data2 = tempfile2.read()
	data3 = tempfile3.read()

	# sulje tiedostot
	tempfile1.close()
	tempfile2.close()
	tempfile3.close()

	# anturi1
	tempdata1 = data1.split("\n")[1].split(" ")[9]
	temp1 = float(tempdata1[2:])
	arvo1 = temp1 / 1000

	# anturi2
	tempdata2 = data2.split("\n")[1].split(" ")[9]
	temp2 = float(tempdata2[2:])
	arvo2 = temp2 / 1000

	# anturit3
	tempdata3 = data3.split("\n")[1].split(" ")[9]
	temp3 = float(tempdata3[2:])
	arvo3 = temp3 / 1000

	print temp1, temp2, temp3

	# change to string for writing	
	s_arvo1 = str(arvo1)
	s_arvo2 = str(arvo2)
	s_arvo3 = str(arvo3)	


	with open("/home/pi/arvot", "w") as tiedosto:
		tiedosto.write(s_arvo1 + "\n" + s_arvo2 + "\n" + s_arvo3 + "\n")

	print s_arvo1, s_arvo2, s_arvo3


	time.sleep(5)


