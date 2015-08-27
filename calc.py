#!/usr/bin/env python
import max7219.led as led
import time 
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT 
from random import randrange 

device = led.matrix(cascaded=4)
device.orientation(90)

#Returns the sum of num1 and num2
def add(num1, num2):
	return num1 + num2

#Returns the result of subtracting num1 - num2
def sub(num1, num2):
	return num1 - num2
	
#Returns the result of multiplying num1 * num2
def mul(num1, num2):
	return num1 * num2
	
#Returns the result of dividing num1 / num2
def div(num1, num2):
	return num1 / num2


def main():
	operation = input("What do you want to do (+,-,*,/): ")
	if(operation != '+' and  operation != '-' and operation != '*' and operation != '/'):
		#invalid operation
		print("You must enter a valid operation")
	else:
		var1 = int(input("Enter num1: "))
		var2 = int(input("Enter num2: "))
		if(operation == '+'):
			print(add(var1, var2))
		elif(operation == '/'):
			print(div(var1, var2))
		elif(operation == '-'):
			print(sub(var1, var2))
		else:
			print(mul(var1, var2))
	
main()