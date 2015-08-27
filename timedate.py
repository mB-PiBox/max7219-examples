#!/usr/bin/env python

#	name = "timedate",
#   version = "0.0.1",
#   author = "Marshall Baer",
#   author_email = "marshallbaer@outlook.com",
#   description = ("A simple clock + date"),
#   license = "MIT"

import max7219.led as led
import datetime
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT 
from random import randrange 

device = led.matrix(cascaded=4) 
device.orientation(90)
device.brightness(1)

while(True):
	clock = time.strftime("%H%M")
	seconds = int(time.strftime("%S"))
	month = time.strftime(" %m")
	day = time.strftime(" %d")
	year = time.strftime("%Y")
	for n, c in enumerate(clock): 
		device.letter(n, ord(c))
	if seconds == 59 :
		for row in range(8):
			device.scroll_up()
			time.sleep(0.1)
		for n, c in enumerate(month): 
			device.letter(n, ord(c))
		time.sleep(1)
		for row in range(8):
			device.scroll_down()
			time.sleep(0.1)
		for n, c in enumerate(day): 
			device.letter(n, ord(c))
		time.sleep(1)
		for row in range(8):
			device.scroll_down()
			time.sleep(0.1)
		for n, c in enumerate(year): 
			device.letter(n, ord(c))
		time.sleep(1)
		for row in range(8):
			device.scroll_down()
			time.sleep(0.1)
		#device.show_message(time.strftime("%b %d %Y"))