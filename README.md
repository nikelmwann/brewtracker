# BrewTracker
An all-in-one solution for continuous monitoring of must or wort temperature,
pH, and (soon) specific gravity during fermentation.

The program running on the ESP8266 reads all of the sensors at set intervals
and reports their values to an external service. Currently this is a set of
ThingSpeak channels to make development and testing easier, but in the future
it will be designed to report to a web application that tracks progress and
provides alerts based on time-sensitive components of recipes (e.g. nutrient
additions).
