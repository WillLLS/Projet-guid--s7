"""
    Installation plug in pymakr pour téléversement vers pycom lopy4
    blink led code :
"""

import pycom
import time

pycom.heartbeat(False)
for cycles in range(10): # stop after 10 cycles
    pycom.rgbled(0x007f00) # green
    time.sleep(0.2)
    pycom.rgbled(0x7f7f00) # yellow
    time.sleep(0.2)
    pycom.rgbled(0x7f0000) # red
    time.sleep(0.2)
    pycom.rgbled(0x7fffff) # 
    time.sleep(0.2)
    pycom.rgbled(0xf00000) # 
    time.sleep(0.2)