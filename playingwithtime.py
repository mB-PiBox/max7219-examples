#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import CP437_FONT
from random import randrange

device = led.matrix(cascaded=4)
device.orientation(90)

device.brightness(8)
while(True):
	device.show_message(time.strftime("%b %d %Y %I:%M"))


	t = (2020, 12, 25, 19, 1, 2, 1, 48, 0)
	t = time.mktime(t)
	print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))
	time.sleep(1)



# while(True): 
#	device.letter(0, ord('F'))
#	device.letter(1, ord('U'))
#	device.letter(2, ord('C'))
#	device.letter(3, ord('K'))
#	time.sleep(0.5)
#
#	device.clear(3)
#	time.sleep(0.5)
#
#	device.clear(2)
#	time.sleep(0.5)
#
#	device.clear(1)
#	time.sleep(0.5)
#
#	device.clear(0)
#	time.sleep(0.5)
