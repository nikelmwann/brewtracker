import time
from machine import Pin

from temperature import TemperatureReader

def start():
    tr = TemperatureReader(208974, 'QYVAZ41CT2D51YJS', Pin(0))
    while True: # test every 5 seconds
        tr.read()
        tr.update()
        time.sleep(5)
