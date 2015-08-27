#!/usr/bin/env python
import max7219.led as led
import time 
import sys 
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT 
from random import randrange 

device = led.matrix(cascaded=4)
device.orientation(90)
#def Hello(name):
	# name = name + '!!!!'
	#device.show_message('Hello ' + name)
	
def four():
	print ('type "clear" to clear word')
	print ('type "exit" to exit script')
	while(True):
		word = raw_input('Enter 4 letter word: (lowercase) ')
		if(word != 'exit' and word != 'clear'):
			device.letter(0, ord(word[0]))
			device.letter(1, ord(word[1]))
			device.letter(2, ord(word[2]))
			device.letter(3, ord(word[3]))
			time.sleep(0.5)
		elif(word == 'clear'):
			device.clear()
		else:
			print ('Exiting Script')
			device.clear()
			break

#Define a main() function that runs when called
#def main():
	#Hello(sys.argv[1])
	
#main()
four()