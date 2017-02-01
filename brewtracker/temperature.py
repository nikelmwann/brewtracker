import time
import urequests
from ds18x20 import DS18X20
from onewire import OneWire

from errors import BrewtrackerError
from util import first

class TemperatureReader:
    def __init__(self, channel_id, api_key, pin):
        self.channel_id = channel_id
        self.api_key = api_key
        self.ds = DS18X20(OneWire(pin))
        self.sensor = first(self.ds.scan())

        if self.sensor is None:
            raise BrewtrackerError("No temperature sensor available!")

        # Last read sensor value in degrees celsius
        self.value = 0

    # Read current value from sensor
    def read(self):
        if self.sensor is not None:
            self.ds.convert_temp()
            time.sleep_ms(750)
            self.value = self.ds.read_temp(self.sensor)
            print(self.value, "degrees celsius")

    # Update ThingSpeak channel with current sensor value
    def update(self):
        data = 'api_key={}&field1={}'.format(self.api_key, self.value)

        r = urequests.post(
                'http://api.thingspeak.com/update',
                data=data,
                headers={
                    'Content-Type': 'application/x-www-form-urlencoded'
                })

        if r.status_code == 200:
            if r.text != '0':
                print('Updated ThingSpeak channel feed with entry', r.text)
        else:
            print('Failed to update ThingSpeak channel feed. Response code:',
                  r.status_code)
