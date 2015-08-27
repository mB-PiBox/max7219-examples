#!/usr/bin/env python
import max7219.led as led
import time 
import sys 
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT 
from random import randrange 

device = led.matrix(cascaded=4)
device.orientation(90)
#def Hello(name):
#	name = name + '!!!!'
#	device.show_message('Hello ' + name)
	
#def four():
#	print ('type "clear" to clear word')
#	print ('type "exit" to exit script')
#	while(True):
#		word = raw_input('Enter 4 letter word: (lowercase) ')
#		if(word != 'exit' and word != 'clear'):
#			device.letter(0, ord(word[0]))
#			device.letter(1, ord(word[1]))
#			device.letter(2, ord(word[2]))
#			device.letter(3, ord(word[3]))
#			time.sleep(0.5)
#		elif(word == 'clear'):
#			device.clear()
#		else:
#			print ('Exiting Script')
#			device.clear()
#			break

def four2():
	loop = True
	while(loop):
		a = []
		print ('')
		print ('Think Of A Four Letter Word...')
		time.sleep(0.5)
		a.append(raw_input('Enter First Letter: '))
		a.append(raw_input('Enter Second Letter: '))
		a.append(raw_input('Enter Third Letter: '))
		a.append(raw_input('Enter Forth Letter: ')) 
		if(a[0] == 'e' and a[1] == 'x' and a[2] == 'i' and a[3] == 't'):
			print ('Exiting Script')
			device.clear()
			break			
		else:
			print ('Flashing '+ a[0] + a[1] + a[2] + a[03])
			time.sleep(1)
			device.letter(0, ord(a[0]))
			device.letter(1, ord(a[1]))
			device.letter(2, ord(a[2]))
			device.letter(3, ord(a[3]))
			time.sleep(0.5)
			device.clear()
			time.sleep(0.5)
			device.letter(0, ord(a[0]))
			device.letter(1, ord(a[1]))
			device.letter(2, ord(a[2]))
			device.letter(3, ord(a[3]))
			time.sleep(0.5)
			device.clear()
			time.sleep(0.5)
			device.letter(0, ord(a[0]))
			device.letter(1, ord(a[1]))
			device.letter(2, ord(a[2]))
			device.letter(3, ord(a[3]))
			time.sleep(0.5)

			print ('')
			while(True):
				again = raw_input('New word? ')
				if (again == 'Y'):
					device.clear()
					break
				elif (again == 'N'):
					loop = False
					print ('Exiting Script')
					time.sleep(0.5)
					device.clear()
					break
				else:
					print ('Enter Y or N')
					time.sleep(0.5)

#Define a main() function that runs when called
#def main():
#	Hello(sys.argv[1])
	
#main()
#four()
four2()