#!/usr/bin/env python

import max7219.led as led
import time
from max7219.font import proportional, SINCLAIR_FONT, TINY_FONT, CP437_FONT
from random import randrange

device = led.matrix(cascaded=4)
device.orientation(90)

device.scroll_up(ord('A'))
