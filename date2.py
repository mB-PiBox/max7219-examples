#!/usr/bin/env python
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
	for n, c in enumerate(year): 
			device.scroll_up(device.letter(n, ord(c)))
			time.sleep(0.1)