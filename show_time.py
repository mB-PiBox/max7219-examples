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
	for n, c in enumerate(clock): 
		device.letter(n, ord(c))
	time.sleep(5)
	#for _ in range(2):
		#for increaseintensity in xrange(5):
		#	device.brightness(increaseintensity)
		#	time.sleep(0.1)
		#for decreaseintensity in xrange(1):
		#	device.brightness(decreaseintensity)
		#	time.sleep(0.1)
	#time.sleep(60)
	#for row in range(8): # 8 = number of rows to scroll down
		#device.scroll_down()
		#time.sleep(.05) # controls scroll down speed
	#device.show_message(time.strftime("%b. %d"))
	#time.sleep(1)

##############################TESTING BELOW##################################
	
	#for n, i in list(enumerate(clock))[::-1]:
		#print i

# while(True):
	# clock = datetime.datetime.now().strftime("%I%M")
	# for n, c in enumerate(clock): 
		# device.letter(n, ord(c))
		# time.sleep(1)
		# for intensity in xrange(5):
			# device.brightness(intensity)
			# time.sleep(0.1)
	# for row in range(8):
		# device.scroll_down(8)
		# time.sleep(.5)
	# device.show_message(time.strftime("%b %d %Y"))
	
# while(True):
	# clock = datetime.datetime.now().strftime("%I%M")
	# for n, c in enumerate(clock): 
		# device.letter(n, ord(c))
	# time.sleep(1)
	# for intensity in xrange(5):
		# device.brightness(intensity)
		# time.sleep(0.1)
	# for row in range(8):
		# device.scroll_down(8)
		# time.sleep(.5)
	# device.show_message(time.strftime("%b %d %Y"))

	
