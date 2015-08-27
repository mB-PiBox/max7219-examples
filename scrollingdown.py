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
	device.letter(0, ord('X'))
	device.letter(1, ord('O'))
	device.letter(2, ord('X'))
	device.letter(3, ord('O'))
	time.sleep(1)
	for row in range(8): # 8 = number of rows to scroll down
		device.scroll_down()
		time.sleep(.5) # controls scroll down speed
		device.flush()
