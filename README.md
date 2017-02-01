# BrewTracker
An all-in-one solution for continuous monitoring of must or wort temperature,
pH, and (soon) specific gravity during fermentation.

## Design
The circuit consists of an ESP8266 running
[MicroPython](http://micropython.org/), an ADC, and a set of sensors
(temperature, pH, etc). Detailed designs can be found under the
[design](design) folder.

## Operation
A program running on the ESP8266 reads all of the sensors at set intervals and
reports their values to an external service.

Currently the "service" is a set of [ThingSpeak](https://thingspeak.com/)
channels to make development and testing easier, but in the future it will be
designed to report to a web application that tracks progress and provides
alerts based on time-sensitive components of recipes (e.g. nutrient additions).
