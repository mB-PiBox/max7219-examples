#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import CP437_FONT
from random import randrange

device = led.matrix(cascaded=4)
device.orientation(90)

device.show_message('Shelly')

device.letter(0, ord('I'))
device.letter(1, ord('S'))
device.letter(2, ord(' '))
device.letter(3, ord('A'))
time.sleep(0.7)
device.clear()

device.show_message('Whore')
device.clear()

device.letter(0, ord('!'))
device.letter(1, ord('F'))
device.letter(2, ord('U'))
device.letter(3, ord('!'))
time.sleep(0.5)

device.clear()
 
time.sleep(0.5)

device.letter(0, ord('F'))
device.letter(1, ord('U'))
device.letter(2, ord('C'))
device.letter(3, ord('K'))
time.sleep(0.4)
device.clear()

device.letter(0, ord('Y'))
device.letter(1, ord('O'))
device.letter(2, ord('U'))
device.letter(3, ord('!'))
time.sleep(0.4)
device.flush()

device.show_message('   ')
device.clear()
