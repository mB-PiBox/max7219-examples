#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import CP437_FONT
from random import randrange

device = led.matrix(cascaded=4)
device.orientation(90)
device.brightness(2)
device.letter(0, 3)
time.sleep(.1)
device.letter(1, 3)
time.sleep(.1)
device.letter(2, 3)
time.sleep(.1)
device.letter(3, 3)
time.sleep(.1)
device.letter(1, ord('8'))
time.sleep(.1)
device.letter(2, ord('3'))
time.sleep(.1)
device.letter(3, ord('1'))

#device.show_message('831')
time.sleep(1)
device.clear()
device.letter(3, 3)
device.show_message('Ashley')
device.clear()

