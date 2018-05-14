from machine import Pin

import time

RUN = Pin(35, Pin.IN)
while 0 == RUN.value():
	time.sleep(0.5)
	