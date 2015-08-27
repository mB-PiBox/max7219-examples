#!/usr/bin/env python
import max7219.led as led
import time 
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT 
from random import randrange 

device = led.matrix(cascaded=4)
device.orientation(90)

print("Hello There Stranger!")
name = raw_input("What is your name? ")
var = input("Enter a number: ")
#device.show_message('Hello '+ name)

#conditional lesson 3
# == EQUALS
# != NOT EQUAL

#if(name == "Marshall"):
if(name == "Marshall" and var == 0):
	device.show_message('Hello Master')
	#print('Hello Master')
elif(name == "Shelly"):
	device.show_message(name +' is a WHORE!')
	#print(name +' is a WHORE!')
else:
	device.show_message('Hello '+ name)
	#print('Hello '+ name)