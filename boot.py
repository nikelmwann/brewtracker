# This file is executed on every boot (including wake-boot from deepsleep)
import esp
esp.osdebug(None)

import gc
# import webrepl
import network
import os
import errno

def connect(ssid, password):
    # disable ap if active
    ap = network.WLAN(network.AP_IF)
    ap.active(False)

    sta = network.WLAN(network.STA_IF)
    if not sta.isconnected():
        print('Connecting to network with ssid "{}"...'.format(ssid))
        sta.active(True)
        sta.connect(ssid, password)
        while not sta.isconnected():
            pass # wait for connection

    print('Network configuration: ', sta.ifconfig())

print('Attempting to connect to configured wifi network...')
try:
    with open('wifi.txt', 'r') as conf:
        lines = list(map(lambda l: l.replace('\n', ''), conf.readlines()))

        if len(lines) < 2:
            print('Wifi configuration is invalid.')
        else:
            connect(lines[0], lines[1])
            print('Setup complete!')
            # webrepl.start()
except OSError as e:
    if e.args[0] == errno.ENOENT:
        print('Wifi configuration does not exist. '
              'Ensure "wifi.txt" is present in the root of the filesystem.')
    else:
        print('Wifi configuration could not be read.')
        print(e)
except Exception as e:
    print('Wifi configuration could not be read.')
    print(e)

gc.collect()
